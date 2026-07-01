"""pandas problem specs."""

PROBLEMS = [
    {
        "slug": "01_double_series",
        "track": "pandas", "difficulty": "easy",
        "title": "Double a Series",
        "tags": ["pandas", "series"],
        "description": "Given a list of numbers, return a pandas Series with each value doubled.",
        "examples": "list(double_series([1, 2, 3])) -> [2, 4, 6]",
        "hint": "pd.Series(values) * 2 vectorizes the doubling.",
        "syntax_hint": "import pandas as pd; return pd.Series(values) * 2",
        "signature": "def double_series(values: list) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    s = double_series([1, 2, 3])\n"
            "    assert isinstance(s, pd.Series)\n"
            "    assert list(s) == [2, 4, 6]\n"
            "    assert list(double_series([])) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import pandas as pd\n\n"
            "def double_series(values: list) -> pd.Series:\n"
            "    return pd.Series(values) * 2\n"
        ),
    },
    {
        "slug": "02_filter_dataframe",
        "track": "pandas", "difficulty": "easy",
        "title": "Filter a DataFrame",
        "tags": ["pandas", "dataframe"],
        "description": "Given a DataFrame with an 'age' column, return rows where age >= 18.",
        "examples": "adults(df) -> df with only age >= 18",
        "hint": "Boolean indexing: df[df['age'] >= 18].",
        "syntax_hint": "df[df['age'] >= 18]",
        "signature": "def adults(df) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({'name': ['a', 'b', 'c'], 'age': [10, 18, 21]})\n"
            "    out = adults(df)\n"
            "    assert list(out['name']) == ['b', 'c']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def adults(df):\n"
            "    return df[df['age'] >= 18]\n"
        ),
    },
    {
        "slug": "03_groupby_mean",
        "track": "pandas", "difficulty": "medium",
        "title": "GroupBy Mean",
        "tags": ["pandas", "groupby"],
        "description": "Given a DataFrame with 'dept' and 'salary', return a Series of mean salary per dept (sorted by dept name).",
        "examples": "mean_salary(df) -> Series indexed by dept",
        "hint": "df.groupby('dept')['salary'].mean().sort_index().",
        "syntax_hint": "df.groupby('dept')['salary'].mean().sort_index()",
        "signature": "def mean_salary(df) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({'dept': ['a', 'a', 'b'], 'salary': [10, 20, 30]})\n"
            "    out = mean_salary(df)\n"
            "    assert out['a'] == 15.0\n"
            "    assert out['b'] == 30.0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def mean_salary(df):\n"
            "    return df.groupby('dept')['salary'].mean().sort_index()\n"
        ),
    },
    {
        "slug": "04_fill_missing",
        "track": "pandas", "difficulty": "easy",
        "title": "Fill Missing Values",
        "tags": ["pandas"],
        "description": "Given a Series with NaN values, return a Series where NaN is replaced by 0.",
        "examples": "fill_zero(s) -> Series with no NaN",
        "hint": "s.fillna(0).",
        "syntax_hint": "s.fillna(0)",
        "signature": "def fill_zero(s) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    import numpy as np\n"
            "    s = pd.Series([1.0, np.nan, 3.0])\n"
            "    out = fill_zero(s)\n"
            "    assert list(out) == [1.0, 0.0, 3.0]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def fill_zero(s):\n"
            "    return s.fillna(0)\n"
        ),
    },
    {
        "slug": "05_value_counts",
        "track": "pandas", "difficulty": "easy",
        "title": "Value Counts",
        "tags": ["pandas"],
        "description": "Return the counts of each unique value in a Series, sorted by count descending.",
        "examples": "counts(pd.Series([1,1,2])) -> {1:2, 2:1}",
        "hint": "s.value_counts() returns a Series sorted descending.",
        "syntax_hint": "s.value_counts().to_dict()",
        "signature": "def counts(s) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    out = counts(pd.Series([1, 1, 2]))\n"
            "    assert out == {1: 2, 2: 1}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def counts(s) -> dict:\n"
            "    return s.value_counts().to_dict()\n"
        ),
    },
    {
        "slug": "06_new_column",
        "track": "pandas", "difficulty": "easy",
        "title": "Add a Computed Column",
        "tags": ["pandas", "dataframe"],
        "description": "Given a DataFrame with 'price' and 'qty', return it with a new 'total' column = price * qty.",
        "examples": "with_total(df) -> df with 'total'",
        "hint": "df.assign(total=df['price']*df['qty']) or df['total']=....",
        "syntax_hint": "df['total'] = df['price'] * df['qty']; return df",
        "signature": "def with_total(df) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({'price': [2, 3], 'qty': [4, 5]})\n"
            "    out = with_total(df.copy())\n"
            "    assert list(out['total']) == [8, 15]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def with_total(df):\n"
            "    df = df.copy()\n"
            "    df['total'] = df['price'] * df['qty']\n"
            "    return df\n"
        ),
    },
    {
        "slug": "07_sort_values",
        "track": "pandas", "difficulty": "easy",
        "title": "Sort Values",
        "tags": ["pandas"],
        "description": "Return the DataFrame sorted by the given column ascending.",
        "examples": "sort_by(df, 'age') -> df sorted by age",
        "hint": "df.sort_values(column).",
        "syntax_hint": "df.sort_values(column).reset_index(drop=True)",
        "signature": "def sort_by(df, column: str) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({'age': [30, 18, 21]})\n"
            "    out = sort_by(df, 'age')\n"
            "    assert list(out['age']) == [18, 21, 30]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def sort_by(df, column: str):\n"
            "    return df.sort_values(column).reset_index(drop=True)\n"
        ),
    },
    {
        "slug": "08_merge_frames",
        "track": "pandas", "difficulty": "medium",
        "title": "Merge Two Frames",
        "tags": ["pandas", "merge"],
        "description": "Merge two DataFrames on the 'id' column (inner join) and return the result.",
        "examples": "merge_on_id(left, right) -> merged df",
        "hint": "pd.merge(left, right, on='id').",
        "syntax_hint": "pd.merge(left, right, on='id')",
        "signature": "def merge_on_id(left, right) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    left = pd.DataFrame({'id': [1, 2], 'name': ['a', 'b']})\n"
            "    right = pd.DataFrame({'id': [1, 2], 'score': [10, 20]})\n"
            "    out = merge_on_id(left, right)\n"
            "    assert list(out.columns) == ['id', 'name', 'score']\n"
            "    assert len(out) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import pandas as pd\n\n"
            "def merge_on_id(left, right):\n"
            "    return pd.merge(left, right, on='id')\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_series_basics",
        "track": "pandas", "difficulty": "easy",
        "title": "Pandas Series Basics",
        "tags": ["pandas", "series"],
        "exercise": "content/problems/pandas/easy/01_double_series.py",
        "body": (
            "# Pandas Series\n\n"
            "A `Series` is a one-dimensional array with an index.\n\n"
            "```python\nimport pandas as pd\ns = pd.Series([1, 2, 3])\n```\n\n"
            "## Vectorized ops\n\n"
            "```python\ns * 2        # [2, 4, 6]\ns.mean()    # 2.0\n```\n\n"
            "Prefer vectorized operations over looping — they are shorter and faster."
        ),
    },
]
