label Chapter_006_branch002_001:
    stop music fadeout 1.0
    play music "Soundtracks/015 - Dying World.mp3" fadein 1.0
    " Tôi nhìn ngược, nhìn xuôi, nhìn ngang, nhìn ngửa một lúc lâu. Không có ai ở đây cả. rút tập tài liệu trong người ra."

    A"  Đây ạ."

    " Paul nhận lấy tập tài liệu, lật qua lật lại từ đầu đến cuối hồi lâu, rồi lần giở một trang bất kỳ và bắt đầu đọc."
    " Và rồi dường như thời gian quanh tôi đã đóng băng. "
    " Paul đứng yên như một bức tượng, chỉ thi thoảng lắc lắc mái đầu muối tiêu làm ra vẻ không tán thành."
    " Rồi ông ta cuộn tập giấy lại thành ống rồi nhét vào chiếc túi ruột tượng."

    show Azu Paul P0 at center
    Pa"  Không ổn. Rất không ổn."
    A"  Có chuyện gì không ổn ạ?"
    show Azu Paul P1 at center
    Pa"  À không, không có gì dính dáng đến cậu. Cậu... làm tốt lắm. Chúng ta sẽ không bao giờ quên những gì cậu đã làm cho chúng ta ngày hôm nay."

    " Khuôn mặt Paul vẫn lạnh, tựa sương đêm ven hồ. Tôi không biết đó là một lời khen khách sáo hay thực chất nữa."

    show Azu Paul P2 at center
    Pa"  Có vẻ cậu vẫn còn thắc mắc nhỉ?"
    A"  Vâng. Còn rất nhiều ạ."

    " Tôi buột miệng mà không kịp suy nghĩ."

    show Azu Paul P0 at center
    Pa"  Ta đoán cậu đã mở cái này-"

    " Ông vỗ vỗ vào chiếc túi ruột tượng."

    show Azu Paul P2 at center
    Pa"  -trước khi đưa cho ta đúng không?"

    " Tôi cúi mặt, gãi gãi đầu như một cậu học trò chưa thuộc bài."

    A"  … Dạ. Nhưng..."
    show Azu Paul P1 at center
    Pa"  Cứ thoải mái, ta không trách cậu. Sự tò mò là đặc tính của vạn vật hữu tri. "
    show Azu Paul P0 at center
    Pa" Và nếu không có sự tò mò và óc quan sát thì không thành người của Aurora được."

    " Tôi định nói là “cháu không hiểu gì hết”."

    show Azu Paul P1 at center
    Pa"  Và ta cam đoan là cậu không hiểu gì hết, đúng không?"

    " … Ấy, chính thế đấy. Tôi bèn lắc đầu."

    A"  Cháu chưa đọc thứ gì rối rắm như thế này bao giờ."
    show Azu Paul P0 at center
    Pa"  Ta không ngạc nhiên. Lý thuyết Hildegard dùng để thảo tài liệu này vượt quá tầm của một nhà khoa học bình thường. "
    show Azu Paul P1 at center
    Pa"  Quá nửa hội chúng ta chưa chắc đã hiểu những gì bà ta viết ở đây."
    A"  Chú có thể giải thích thêm được không ạ?"
    show Azu Paul P0 at center
    Pa"  Ta có thể giành một tháng để giảng giải cặn kẽ cho cậu lý thuyết lượng tử và vũ trụ học để cậu có thể tự đọc và tự hiểu. "
    show Azu Paul P1 at center
    Pa"  Hoặc ta có thể giành năm giây để cho cậu biết cậu đã làm rất tốt."

    if Quantum.Physics == 1:
        call Chapter_006_branch002_001_001 from _call_Chapter_006_branch002_001_001
    else:
        call C006_B002_001_001_B001 from _call_C006_B002_001_001_B001 

    return