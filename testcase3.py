from VL1.VL1 import VL1

"""
Thưa các thầy, đáng lẽ testcase 3 phải là chọn 1 ngẫu nhiên 1 sản phẩm từ menu để đọc mô tả về sản phẩm đó. 
Nhưng trong khi gõ báo cáo thì em ghi nhầm thành Cuộn từ trên xuống trên trang chủ.
Em mong các thầy thông cảm cho sơ suất này ạ :(

Mai Hoàng Anh Vũ
"""

try:
    with VL1() as bot:
        bot.land_first_page()
        bot.open_detail()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows CMD: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Windows Powershell: \n'
            '    $env:Path += ";C:path-to-your-folder \n'
            'E.g: \n'
            '     $env:Path += ";C:\\SeleniumDrivers\\" \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/to-your/folder/ \n'
        )
    else:
        raise
