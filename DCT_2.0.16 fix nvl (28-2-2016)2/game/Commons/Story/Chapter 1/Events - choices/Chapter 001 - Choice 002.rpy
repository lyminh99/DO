label Chapter_001_choice_002:
    $ Chapter_001_choice_002_played = 1
    $ Church += 1

#Cảnh: Nhà thờ
#Thời gian: Chiều
#//Delay 1s
    stop music fadeout 1.0
    play music "Soundtracks/007 - Memories - Composed.ogg" fadein 1.0
    scene BG_9 with fade
    $ renpy.pause (2.0)
#Cảnh: Thánh đường
#Thời gian: Chiều
#//SFX: Tiếng mở cửa.
    scene BG_1 with fade
    play sound "sfx/door-1-close.mp3" fadein 1.0
    A"  Xin phép ạ."

    "Khung cảnh thánh điện tráng lệ ập vào mắt ngay khi tôi đẩy nhẹ cánh cửa."
    "Nhà thờ ở đây vốn chẳng khóa cổng bao giờ."

    A"  Cha ơi."
    nvlDC"
Tôi khẽ gọi vào thinh không. Đứng một mình dưới những xà nhà cao ngất khiến ta có chút ái ngại, dù cho ánh mắt của đức Chúa trời liên tục ban xuống có ấm áp đến đâu.
Tôi vuốt nhẹ lên những thành ghế xếp ngay ngắn thành từng dẫy. Cứ như thể Cha vừa mới lau dọn sạch sẽ đay thôi.
\n 
\n Chiếc khăn hằng ngày quét qua chúng đang vắt trên thành ghế đầu, nhưng người chủ nhân của nó chẳng hề thấy chút bóng dáng.
Một người cẩn trọng đang trở nên bề bộn. Phải chăng có một việc gì đó khiến ông vội vã rời khỏi đây?
Cả người phụ tá Hanes thường ngày cũng không có ở đây. Cả nhà thờ lớn trở thành một cái lồng trống rỗng.
Một mảnh giấy nhỏ để lại, với nội dung thông báo về sự vắng mặt của mục sư Fredo. 
Việc trở thành một giám mục cấp cao cũng đồng nghĩa với mang trên vai khối lượng công việc khổng lồ. 
\n Cha Fredo, dù đã trên bảy chục tuổi, vẫn phải ngày ngày vác tấm lưng đi đây đi đó. Ai cũng phải nể phục sức khỏe và sự chịu đựng kinh người của ông. 
    "
    nvl clear
#------------------------------------------------
    A"  ..."

    "Tôi đặt mảnh giấy trở lại bàn."
    "Có lẽ tôi không nên làm phiền nơi này lâu hơn nữa. Vốn dĩ tôi cũng chẳng có việc gì ở đây."
    "Cầu nguyện một chút, tôi quay đầu trở ra."

    return