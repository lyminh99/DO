label Chapter_001_choice_003:
    $ Chapter_001_choice_003_played = 1

#Cảnh: Đường phố
#Thời gian: Chiều
    scene BG_6 with fade
    stop music fadeout 1.0
    play music "Soundtracks/011 - My childhood.ogg" fadein 1.0
    "Khu chợ chiều bắt đầu tàn. Tiếng chổi dọn dẹp rải đầy con đường lớn."
    "Mấy con gà lẩn thẩn khi khổng khi không xổng chuồng đứng giữa phố mà ra sức gáy. "
    "Nè nè! Đừng có bu ta. Không có cái gì để mổ đâu. Ế! Nè! Đồ gà mái!"

    C0"  Anatolio!! Oi oi…Anatolio…"

    "Không chỉ có máy con gà liên tục cục tác, mà đến cả người cũng chẳng hề buông tha cho tôi."

    A"  Nè nè. Tớ không có quen cậu đâu nhé."

    "Nhưng mà không sao, ít ra điều này cũng không khó chịu lắm."

    C0"  Sao lại không quen tôi? Hanes đây nè. Cậu không phải là Anatolio sao?"
    A"  Không. Mình là Olionata. Anh em cùng cha khác…ông nội của Anatolio Pietro. Còn bạn là Hanes, phải không?"

#//Hanes trố mắt 1s
    $ renpy.pause (1.0)
    show Azu Hanes P0 at center
    H"  Thế à? Nhưng mà cậu trông giống Anatolio như lột mà."
    A"  Vậy sao? Cậu cũng trông giống người bạn Henas của tớ như tạc vậy."

#//Hanes băn khoăn 1s
    $ renpy.pause (1.0)
    show Azu Hanes P0 at center
    H"  Tôi là Hanes mà."
    A"  Thì tớ là Olionata."
    show Azu Hanes P0 at center
    H"  Ưm. Nhưng mà—"
    A"  Thế này đi cho dễ hiểu, nếu tớ là Anatolio, thì cậu là Henas. "
    A"  Còn nếu tớ là Olionata, thì cậu là Hanes. Như thế đủ dễ hiểu chưa."

#//Hanes băn khoăn 1s
#//Hanes đổi kiểu băn khoăn thêm 1s
    $ renpy.pause (1.0)
    show Azu Hanes P0 at center
    H"  Ô. Tôi hiểu rồi! Tôi là Hanes, vậy cậu đúng không phải là Anatolio rồi. "
    show Azu Hanes P0 at center
    H"  Hay quá, lại gặp anh em của Anatolio ở đây. Xin tự giới thiệu, tôi là Hanes. "
    show Azu Hanes P0 at center
    H"  Rất vui được gặp bạn. Hai bạn trông rất giống nhau đấy. Ta làm bạn được chứ?"
    A"  Hiểu rồi thì tốt. Ai cũng nói với tớ như vậy."

    "Bởi vì tớ là Anatolio mà."

    A"  À. Tớ cũng cảm thấy bạn thật đặc biệt đấy. Nếu chúng ta làm bạn thì thật là tốt biết bao."

    "Bạn thật đặc biệt vì trừ bạn ra chẳng ai tin câu nói vừa rồi của tớ đâu."
    "Thôi, quay lại vấn đề, chàng trai đẹp mã chỉ-thua-tôi trong bộ áo cổ rùa vừa bắt gặp tôi bị mấy con gà ăn hiếp "
    "là một thằng bạn nối khố từ khi cả hai còn mặc tả ám hại nhau. "
    "Hanes là tên chúng tôi vẫn gọi cậu ta, và do cặp vợ chồng nhận nuôi không đặt họ cho cậu ấy "
    "nên Hanes vẫn chỉ được gọi bằng tên, dù là người quen hay lạ."

    show Azu Hanes P0 at center
    H"  Thật-Thật tốt quá. Oli-lionata."

    "Hanes nắm lấy tay tôi, hồ hởi như mới quen thật. Cậu chàng còn đọc nhầm tên tôi thành li-li nữa chứ."
    "Tuy nhiên, ấn tượng của tôi về Hanes không chỉ có vậy. "
    "Một đặc điểm nhận dạng rõ rệt hơn là cái bộ đầu tóc trắng như bạch kim và đôi mắt màu đỏ hồng của hắn. "
    "Chúng mới thực là có một không hai. Màu trắng, cái màu quá hợp cho bộ óc ngô nghê không tạp nhiễm của hắn vậy. "
    "Nói đi cũng phải nói lại, sự “đặc biệt” ấy cũng gây cho Hanes không ít phiền phức. "
    "Phiền toái nhất là việc hắn không tìm được việc làm. Mọi người đều cảm thấy hắn vô cùng quái dị. "
    "Nếu không có Cha Fredo giúp đỡ, chắc hắn cũng đã thành kẻ ăn bám như tôi rồi. Mà nhà hắn làm gì có tiền cơ chứ."
    "Cũng phải cảm ơn Cha, kể từ đó, Hanes trở thành phụ tá cho nhà thờ, cậu ấy ở đó luôn cũng từ dạo ấy."
    "Nói mới nhớ, hình như lâu rồi tôi không còn gặp cậu ta nữa."
    "Lâu rồi không gặp, tôi lại lợi dụng cậu ta làm công cụ xả stress, hình như không được hay ho cho lắm."

    "Có lẽ tôi nên:"
    menu:
        "Nói thật cho cậu ta":
            call Chapter_001_choice_003_C001 from _call_Chapter_001_choice_003_C001
        "Tiếp tục gạt cho đến cùng":
            call Chapter_001_choice_003_C002 from _call_Chapter_001_choice_003_C002
    return