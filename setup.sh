mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor=\"#f63366\"\n\
backgroundColor=\"#ffffff\"\n\
secondaryBackgroundColor=\"#d9dcde\"\n\
textColor=\"#262730\"\n\
font=\"sans serif\"\n
" > ~/.streamlit/config.toml
