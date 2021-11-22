# Kiểm thử tự động cho website VL1 Project POS Restaurant
## Giới thiệu về công cụ Selenium Webdriver nhóm sử dụng
Selenium WebDriver là một automation framework 
dành cho web dùng để thực hiện các 
phiên kiểm thử của mình trên các trình duyệt khác nhau 
mà không cần chỉ giới hạn trên Firefox hay Chrome.

Selenium WebDriver sẽ cung cấp công cụ hỗ trợ tốt 
trong việc coding để tạo test scripts.

Selenium WebDriver hỗ trợ nhiều ngôn ngữ lập trình khác nhau 
như Java, .Net, PHP,Python, Perl, Ruby . . .

Trong bài tập lớn này, nhóm sử dụng ngôn ngữ Python 
và trình duyệt Chrome để kiểm thử tự động trang web VL1 Restaurant.
## Cách tải về
Dùng terminal và gõ lệnh sau
```commandline
git clone https://github.com/jesuisjohan/CNPM-testing.git
```
## Tải về WebDriver cho trình duyệt Google Chrome
Truy cập trang web sau 
và chọn phiên bản phù hợp với phiên bản hiện tại 
của trình duyệt Chrome trên máy tính

https://chromedriver.storage.googleapis.com/index.html

Sau khi tải về thì cần thay đổi biến **driver_path** của hàm __init__
trong class VL1 của file VL1.py
## Tải về các package cần thiết
```commandline
pip install -r requirement.txt
```
## Chỉnh sửa PATH để chạy chương trình
Trên Windows, dùng powershell để chạy lệnh sau
```commandline
$env:Path += ";C:path-to-your-folder
```
Ví dụ:
```commandline
$env:Path += ";C:\SeleniumDrivers\"
```
## Chạy các testcase
Chạy các testcase bằng Python

Ví dụ:
```commandline
python testcase1.py
```