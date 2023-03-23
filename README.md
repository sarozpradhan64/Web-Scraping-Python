## Scrape All Jobs In Nepal

## Installation

### Next.js
``` 
cd frontend
npm install
npm run dev
```
### Fast API
-Note: Virtual env is suggested
```
pip install requests
pip install beautifulsoup4
pip install fastapi
pip install "uvicorn[standard]"
```
- Or install via requirements.txt
```
cd core
pip install -r requirements.txt
```

### Run FastApi Server
```
cd core
uvicorn main:app --reload
```