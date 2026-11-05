# CryptoRespect

CryptoRespect is a French Python desktop application that allows users to monitor cryptocurrency market data and visualize price trends through an interactive graphical interface.


Built with Tkinter, Matplotlib, and the CoinGecko API, the application lets users select a cryptocurrency, choose a currency, and display historical market data over multiple time periods.

---

## Features

- View cryptocurrency market information
- Display market capitalization in multiple currencies
- Interactive price history graphs
- Support for different time ranges:
  - 1 hour
  - 1 day
  - 1 week
  - 1 month
  - 6 months
  - 1 year
- Cryptocurrency logo display
- Simple and intuitive graphical user interface

---

## Supported Cryptocurrencies

Currently supported:

- Bitcoin (BTC)
- Ethereum (ETH)
- BNB
- Official Trump (TRUMP)
- Shiba Inu (SHIB)

---

## Supported Currencies

- USD
- EUR
- GBP
- INR
- KRW
- JPY
- MXN

---

## Technologies Used

- Python
- Tkinter
- Pillow (PIL)
- Requests
- Matplotlib
- CoinGecko API

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Z19Z19/Crypto-Respect.git
cd Crypro-Respect
```

### 2. Install dependencies

```bash
pip install requests pillow matplotlib
```

### 3. Prepare the image directory

Create an `Images` folder containing:

```text
Images/
├── Bitcoin.png
├── ETH.png
├── BNB.png
├── Shiba.png
└── Trump.png

---

## Running the Application

Execute:

```bash
python CryptoRespect.py
```

The graphical interface will open automatically.

---

## How It Works

1. Select a cryptocurrency from the left dropdown menu.
2. Select a currency from the right dropdown menu.
3. Click one of the time-period buttons.
4. The application:
   - Retrieves market data from CoinGecko.
   - Displays the cryptocurrency's market capitalization.
   - Generates a graph showing price evolution over the selected period.
   - Updates the cryptocurrency image.

---

## Project Structure

```text
CryptoRespect/
│
├── CryptoRespect.py
├── cryptorespect.png
├── README.md
│
└── Images/
    ├── Bitcoin.png
    ├── ETH.png
    ├── BNB.png
    ├── Shiba.png
    └── Trump.png
```

---

## API

This project uses the CoinGecko API.

Market information is retrieved through the `/coins/markets` endpoint and historical data through the `/market_chart/range` endpoint.

---

## Author

**Zaki Dufournet**

---

## License

This project is intended for educational purposes.
