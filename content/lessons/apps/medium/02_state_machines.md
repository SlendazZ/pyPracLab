---
title: State Machines in Applications
track: apps
difficulty: medium
tags: state-machine
exercise: content/problems/apps/medium/08_pomodoro_state.py
---

# State Machines in Applications

## Overview

Many app workflows are finite state machines: orders (pending → paid → shipped), tickets (open → in progress → closed), games (menu → playing → game over). Explicit states prevent impossible transitions.

A boolean flag per concern (`is_paid`, `is_shipped`, `is_cancelled`) explodes into illegal combinations — paid and cancelled at once. A state machine allows exactly one current state and defines which moves are legal.

Think of states as rooms and transitions as doors. You can only walk through doors that exist; the transition table is the floor plan.

## Modeling states

`Enum` gives named constants and blocks typos like `'PENDNG'`:

```python
from enum import Enum, auto

class OrderState(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELLED = auto()
```

Compare with `is` or `==` — never compare to raw strings loaded from a database without validating first:

```python
def parse_state(name: str) -> OrderState:
    try:
        return OrderState[name]
    except KeyError:
        raise ValueError(f'unknown state: {name}')
```

## Transition table

Encode allowed edges in one data structure. Every transition goes through one function:

```python
ALLOWED = {
    OrderState.PENDING: {OrderState.PAID, OrderState.CANCELLED},
    OrderState.PAID: {OrderState.SHIPPED},
    OrderState.SHIPPED: set(),
    OrderState.CANCELLED: set(),
}

def transition(order, new_state: OrderState) -> None:
    allowed = ALLOWED[order.state]
    if new_state not in allowed:
        raise ValueError(
            f'cannot go {order.state.name} -> {new_state.name}'
        )
    order.state = new_state
```

Terminal states (`SHIPPED`, `CANCELLED`) have empty allowed sets — no way out without adding a new business rule.

Draw the table as a diagram while learning:

```
PENDING ──→ PAID ──→ SHIPPED
   │
   └──→ CANCELLED
```

## Worked example: Order object with history

Wrap state in a class so callers cannot assign `order.state` directly:

```python
from dataclasses import dataclass, field
from enum import Enum, auto

class OrderState(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELLED = auto()

ALLOWED = {
    OrderState.PENDING: {OrderState.PAID, OrderState.CANCELLED},
    OrderState.PAID: {OrderState.SHIPPED},
    OrderState.SHIPPED: set(),
    OrderState.CANCELLED: set(),
}

@dataclass
class Order:
    id: int
    state: OrderState = OrderState.PENDING
    history: list[str] = field(default_factory=list)

    def advance(self, new_state: OrderState) -> None:
        if new_state not in ALLOWED[self.state]:
            raise ValueError(f'{self.state.name} -> {new_state.name} not allowed')
        self.history.append(f'{self.state.name} -> {new_state.name}')
        self.state = new_state
```

Walk through a happy path:

```python
order = Order(id=1)
order.advance(OrderState.PAID)
order.advance(OrderState.SHIPPED)
order.history
# ['PENDING -> PAID', 'PAID -> SHIPPED']

order.advance(OrderState.CANCELLED)  # ValueError
```

Step by step:
1. New orders start in `PENDING`.
2. `advance` checks the table before mutating.
3. `history` records an audit trail for support and debugging.
4. Illegal moves raise immediately instead of corrupting data.

List legal next moves for UI buttons:

```python
def available_actions(order: Order) -> list[OrderState]:
    return sorted(ALLOWED[order.state], key=lambda s: s.name)

available_actions(Order(id=1))
# [OrderState.PAID, OrderState.CANCELLED]
```

## Worked example: timer states (Pomodoro-style)

The same pattern fits UI timers with fewer states:

```python
from enum import Enum, auto

class TimerPhase(Enum):
    IDLE = auto()
    RUNNING = auto()
    PAUSED = auto()
    FINISHED = auto()

TIMER_ALLOWED = {
    TimerPhase.IDLE: {TimerPhase.RUNNING},
    TimerPhase.RUNNING: {TimerPhase.PAUSED, TimerPhase.FINISHED},
    TimerPhase.PAUSED: {TimerPhase.RUNNING, TimerPhase.IDLE},
    TimerPhase.FINISHED: {TimerPhase.IDLE},
}

def advance_timer(phase: TimerPhase, event: str) -> TimerPhase:
    targets = {
        'start': TimerPhase.RUNNING,
        'pause': TimerPhase.PAUSED,
        'finish': TimerPhase.FINISHED,
        'reset': TimerPhase.IDLE,
    }
    new = targets[event]
    if new not in TIMER_ALLOWED[phase]:
        raise ValueError(f'cannot {event} while {phase.name}')
    return new
```

Map button clicks to events (`start`, `pause`, `reset`) and only enable buttons when the event is legal from the current phase.

Walk through a session:

```python
phase = TimerPhase.IDLE
phase = advance_timer(phase, 'start')    # RUNNING
phase = advance_timer(phase, 'pause')    # PAUSED
phase = advance_timer(phase, 'start')    # RUNNING again
phase = advance_timer(phase, 'finish')   # FINISHED
phase = advance_timer(phase, 'reset')    # IDLE
advance_timer(phase, 'pause')            # ValueError — cannot pause while IDLE
```

## Benefits

- Business rules live in one place (the transition table)
- Easy to diagram and review with stakeholders
- Tests cover every allowed and forbidden edge in a loop

```python
def test_all_illegal_transitions():
    for src in OrderState:
        for dst in OrderState:
            if dst not in ALLOWED[src]:
                order = Order(id=0, state=src)
                try:
                    order.advance(dst)
                except ValueError:
                    pass
                else:
                    raise AssertionError(f'{src} -> {dst} should fail')
```

This loop tests every forbidden edge automatically — add a new state and the test still covers it.

## Persisting state safely

When saving to a database or file, store the enum name as a string:

```python
def order_to_dict(order: Order) -> dict:
    return {'id': order.id, 'state': order.state.name, 'history': order.history}

def order_from_dict(data: dict) -> Order:
    return Order(
        id=data['id'],
        state=OrderState[data['state']],
        history=list(data.get('history', [])),
    )
```

Always validate on load — never trust raw strings from storage.

## UI connection

Enable buttons only for valid transitions. Display current state clearly — users should never wonder whether an order is paid or merely pending.

```python
def button_enabled(order: Order, action: OrderState) -> bool:
    return action in ALLOWED[order.state]
```

## Common pitfalls

- Scattering `if status == ...` across dozens of files
- Allowing backward transitions without explicit business approval
- Persisting state as free-form strings without validation on load
- Skipping terminal states in the table (implicit None → anything)
- Letting callers set `.state` directly — route changes through `advance`

## Practice

Implement order state transitions with a validation table.

## Summary

State machine = states + allowed edges + transition function. Use when workflow rules matter more than free-form flags. Centralize the table, route every change through one method, and test illegal paths as thoroughly as happy paths.
