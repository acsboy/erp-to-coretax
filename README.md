# ERP to Core Tax Converter

A web application that converts ERP sales data to Core Tax import format for Indonesian tax compliance.

## 🚀 Features

- **Smart Data Mapping**: Automatically maps your ERP sales data to Core Tax format
- **Tax Calculation**: Calculates DPP (Dasar Pengenaan Pajak) and PPN automatically
- **Web Interface**: Easy-to-use drag & drop file upload interface
- **Fast Processing**: Handles hundreds of transactions in seconds
- **Core Tax Compatible**: Generates exact format required by DJP Core Tax system

## 📋 Supported Data Fields

### Input (Your Sales Data):
- CustomerCode, CustomerName
- InvoiceNo, InvoiceDate
- ItemCode, ItemName
- Qty (Quantity)
- PriceAfterTax, InvoiceAmount

### Output (Core Tax Format):
- Faktur sheet with header information
- DetailFaktur sheet with transaction details
- REF and Keterangan sheets for reference

## 🛠 Technology Stack

- **Backend**: FastAPI (Python)
- **Data Processing**: Pandas, OpenPyXL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Railway.app

## 🚀 Quick Deploy to Railway

### Method 1: One-Click Deploy (Recommended)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/yourusername/erp-to-coretax)

### Method 2: Manual Deploy

1. **Fork this repository** or create a new repository with these files

2. **Connect to Railway**:
   - Go to [Railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Configure Environment** (Optional):
   - Set `PORT` environment variable (Railway sets this automatically)
   - Set `PYTHON_VERSION` to `3.11` if needed

4. **Deploy**:
   - Railway will automatically detect the Python app
   - It will install dependencies from `requirements.txt`
   - The app will be available at your Railway domain

## 🏠 Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd erp-to-coretax
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Open browser**: Navigate to `http://localhost:8000`

## 📁 File Structure

```
erp-to-coretax/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── railway.yml         # Railway deployment config
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── .gitignore          # Git ignore patterns
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8000` |
| `PYTHON_VERSION` | Python version | `3.11` |

### Tax Settings

The application uses these default tax settings (can be modified in `main.py`):
- **PPN Rate**: 12% (Indonesian VAT)
- **Default Item Code**: 310000 (if not provided)
- **Default Unit**: UM.0003

## 📝 Usage Instructions

1. **Access the Web Interface**: Open your Railway app URL
2. **Upload Excel File**: Drag & drop or click to select your Sales.xlsx file
3. **Convert**: Click "Convert to Core Tax Format" button
4. **Download**: Download the generated Core Tax compatible file
5. **Import to Core Tax**: Use the downloaded file in DJP Core Tax system

## 📊 Data Mapping

| Sales Data Field | Core Tax Field | Notes |
|------------------|----------------|-------|
| ItemCode | Kode Barang Jasa | Product/service code |
| ItemName | Nama Barang.Jasa | Product/service name |
| Qty | Jumlah Barang Jasa | Quantity |
| PriceAfterTax | → DPP calculation | Calculates base price |
| InvoiceAmount | → PPN calculation | Calculates tax amount |

## 🔍 API Endpoints

- `GET /` - Web interface
- `POST /convert/` - File conversion endpoint
- `GET /health` - Health check

## 🛡️ Error Handling

The application includes comprehensive error handling for:
- Invalid file formats
- Missing required data
- Calculation errors
- Network issues

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This application is designed to work with standard ERP sales data formats. Please verify the output with your tax consultant before submitting to DJP Core Tax system.

## 🆘 Support

If you encounter issues:
1. Check the Railway logs for error messages
2. Verify your input data format matches the expected structure
3. Contact support for custom data mapping requirements

---

**Made with ❤️ for Indonesian businesses to simplify tax compliance**
