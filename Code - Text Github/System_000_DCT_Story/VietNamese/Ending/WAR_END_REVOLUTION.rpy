label WAR_END_REVOLUTION:

#Chương 7C: Chiến thắng
    stop music fadeout 1.0
    play music "Soundtracks/Demo2_3.mp3" fadein 1.0
    " Mười năm sau."

#Cảnh: Phòng làm việc (Có chăng một lá cờ nền vàng có hình mặt trời đang trồi lên khỏi đỉnh núi)
#Thời gian: Sáng

    show Azu Unknow P0 at center
    HC"  Cấp báo! Cấp báo!"
    show Azu Unknow P0 at center
    HC"  Thưa Đại Tổng thống, chúng ta thắng rồi. Thắng rồi!"
    show Azu Unknow P0 at center
    HC"  Pháo đài cuối cùng của lực lượng Phán quan phía bờ Nam sông Lucina đã giải phóng! "
    show Azu Unknow P0 at center
    HC" Toàn bộ hơn 3000 kỵ binh của Bá tước de Rovere đã bị bắt sống! Những ổ chống cự cuối cùng trong nội thành đã nối nhau ra hàng!"
    show Azu OngPietro at center
    P"  Còn Giáo hoàng và bộ sậu Đôi mắt Ánh sáng thì sao?"
    show Azu Unknow P0 at center
    HC"  Chết cả rồi, thưa Đại Tổng thống!"
    show Azu OngPietro at center
    P"  … Thương vong phe ta thế nào?"
    show Azu Unknow P0 at center
    HC"  Tiểu đoàn 3 bị thiệt hại hơn hai trăm người. Tiểu đoàn 6 có khoảng 50 người hy sinh và 30 người bị thương. "
    show Azu Unknow P0 at center
    HC"  Các đơn vị còn lại thiệt hại không đáng kể, thưa ngài!"
    show Azu OngPietro at center
    P"  Tốt. Ngươi lui đi."
    show Azu Unknow P0 at center
    HC"  Vâng, thưa Tổng thống!"
    show Azu OngPietro at center
    P"  Ngươi cũng lui đi."
    show Azu Unknow P1 at center
    TK"  Vâng, thưa ngài."

    " …"
    " Paul ngả lưng lên ghế, cằm khẽ hướng lên trần phòng."

    show Azu OngPietro at center
    P"  Ta hy vọng đây sẽ là những người cuối cùng hy sinh trong cuộc chiến này."
    show Azu OngPietro at center
    P"  Mười năm... mười năm là quá ngắn ngủi đối với một thế giới..."
    show Azu OngPietro at center
    P"  Còn cậu, Anatolio. Có lẽ cả đời cậu không bao giờ nghĩ rằng cậu lại khiến thế giới thay đổi nhiều như thế. "
    show Azu OngPietro at center
    P" Càng không nghĩ rằng cậu phải chết để mang lại thay đổi ấy."
    show Azu OngPietro at center
    P"  .. Ta … Rất tiếc."
    show Azu OngPietro at center
    P"  Nhưng cậu chớ lo. Những gì cậu còn chưa làm được trên thế giới này..."

#//Mode:NVL
    nvlDC"
Paul thoáng nhìn xuống tấm kính phủ lên bộ bàn lớn của mình. Ông đặt mắt mình lên ba tập tài liệu chờ ký. "
    nvlDC"\n Đây là tiêu đề của hai trong số chúng:
\n "
    nvlDC"\n “Nghị quyết của Quốc hội"
    nvlDC"\n Về việc Truy tặng Danh hiệu Anh hùng cho Anatolio Pietro”.
\n "
    nvlDC"\n Và:"
    nvlDC"\n “Đề án Nghiên cứu"
    nvlDC"\n Về Không gian Ngoài thế giới"
    nvlDC"\n Chủ nhiệm Đề tài: Tiến sĩ Khoa học Azzurra Ines”.
    "
    nvl clear

#Cảnh: đen
    scene black with fade
    show Azu OngPietro at center
    P"  Chúng ta đã lo liệu đủ cả."

    show fin_white:
     yalign 0
     xalign 0.9
     alpha 0
     linear 2 alpha 1
    $renpy.pause (2)
    hide fin_white 

    return