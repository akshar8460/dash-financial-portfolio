# Dash Financial Portfolio

The Financial Portfolio Tracker is a web application built with Python and Dash framework that allows users to track and manage their investment portfolio. It provides an interactive dashboard with features such as displaying portfolio holdings, calculating portfolio value, and visualizing portfolio performance.

## Features

- Display portfolio holdings with stock symbol, quantity, and purchase price
- Calculate and display the current value of each investment
- Provide an overall portfolio value based on the sum of individual investments
- Interactive and responsive user interface
- Easy-to-use and intuitive design

## Prerequisites

- Python 3.x
- Dash framework
- Pandas library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/akshar8460/dash-financial-portfolio.git
```

2. Navigate to the project directory:

```bash
cd dash-financial-portfolio
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your portfolio data by creating a `portfolio.csv` file with the following columns: "Stock Symbol", "Quantity", and "Purchase Price". See the provided `portfolio.csv` file as an example.

2. Run the portfolio tracker application:

```bash
python portfolio_tracker.py
```

3. Open a web browser and go to `http://127.0.0.1:8050/` to access the portfolio tracker dashboard.

4. The dashboard will display your portfolio holdings, current values, and an overall portfolio value.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

