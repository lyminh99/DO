label Chapter_001_p5_C002_C003:

#Cảnh: thánh điện
#Thời gian: tối
    scene BG_1 with dissolve
    stop music fadeout 1.0
    play music "Soundtracks/015 - Dying World.mp3" fadein 1.0
    "Không!"
    "Tôi vẫn không cảm thấy nó quá thuyết phục, ít nhất là trong tình huống này."
    "Cho dù không rước phiền phức thì Hanes cũng không thể trở thành một người mang lại lợi ích đáng kể nào về việc nghiên cứu cho nhóm chúng tôi."

    A"Cậu còn lý do nào khác không? Đại loại như việc Hanes đến sẽ góp thêm sách vở chẳng hạn."

    "Tôi cố viện ra một cái cớ thật khó khăn."
    show Azu P52 at center
    Az"Về việc này…"
    hide Azu P52 at center
    show Azu Hanes P0 at center
    H"Cái đó thì tôi l-làm được đấy! Tôi thường-thường xuyên đi khắp nơi giữa hai bên thành phố, t-tôi có thể giúp cậu. "
    show Azu Hanes P2 at center
    H"Xin c-cậu đấy, cho t-tôi vào nhóm đi!"

    "Giọng Hanes khẩn thiết cầu xin. Như vậy là tôi không còn lý do gì để không nhận cậu ta nữa."
    "Cả Azu cũng đang bụm môi, nghiến răng kèn kẹt. "
    "Dù vậy, tôi vẫn cảm thấy có gì đó lấn cấn trong đầu."
    "Rốt cục thì tôi có nên cho cậu ấy vào nhóm không?"

    menu:
        "Cho Hanes vào nhóm":
            call Chapter_001_p5_C002_C001 from _call_Chapter_001_p5_C002_C001
        "Cho Hanes vào nhóm":
            call Chapter_001_p5_C002_C001 from _call_Chapter_001_p5_C002_C001_1
        "Cho Hanes vào nhóm":
            call Chapter_001_p5_C002_C001 from _call_Chapter_001_p5_C002_C001_2

    return