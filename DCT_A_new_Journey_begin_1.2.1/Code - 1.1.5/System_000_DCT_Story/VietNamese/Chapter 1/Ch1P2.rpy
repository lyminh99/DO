label Ch1P2:
#Cảnh: Công viên
#Thời gian: Chiều
    stop music fadeout 1.0
    play music "Soundtracks/004 - Lovely Bubbles.ogg" fadein 1.0
    scene BG_6 with dissolve

    " Dãy phố này là nơi ánh sáng không bị chặn lại bởi những công trình. Tôi có thể thấy màu trời hoàng hôn từ nơi đây."
    " Những lúc cảm thấy ngột ngạt với những dãy tường xám ngoét, tôi lại dạo quanh nơi đây, "
    " ngắm những nhà cửa tầng tầng lớp lớp nối tiếp nhau, cùng lúc thưởng thức mùi màu vẽ với cây cọ trên tay."
    " Chào mừng đến với xưởng vẽ của Anatolio này. "
    " Tranh của tôi lúc nhỏ luôn được người xung quanh tán thưởng."
    " Cho đến tận giờ, ngày tháng ấy như chỉ mới hôm qua."
     
#//Màn hình nẩy lên 5s
    with sshake3

    stop music fadeout 1.0
    A"  !!!"

    "Động đất sao?"
    "Tôi có thể trông thấy đám đông đang nhốn nháo đằng kia."
    "Có lẽ tôi cũng phải chạy sớm ra khỏi chỗ này, kiếm cái gầm ghế nào đó mà núp."

    C0" ĐỘNG ĐẤT!!! TRÁNH RA ĐI!!!!"
    A"  Hể? Động đất biết thông báo sao?"

    "Không. Giọng nói này quen lắm."
    "Tôi lách người sang bên. Ngay phía sau tôi, chẳng biết từ đâu, có sẵn một cái ổ gà cực to."

#//Màn hình nảy lên.
    with sshake
    C0" Ui da."

    " Tôi nhận ra hình dáng quen thuộc đang ngã sóng xoài dưới đất. Cô gái trẻ, trạc tuổi tôi, với mái tóc vàng sẫm bóng như dầu. "
    " Cô chổng mông, phủi phủi cẳng chân như đang cố gây sự chú ý với những người xung quanh. "
    " Trên tay cô còn ôm quyển sách, bìa màu nâu hạt dẻ, quyết không buông ra."

    A"  Azzurra!"
    show Azu P58 at center    
    AZ"  Anatolio?"

#Cảnh: công viên có ghế đá
#Thời gian: chiều tối
    scene BG_6 with dissolve
    stop music fadeout 1
    play music "Soundtracks/019 - Azzura theme.mp3" fadein 2.0
    "Chúng tôi tìm một khoảng ghế trống ngồi nghỉ chân. Thật may Azzurra chỉ bị xây xác nhẹ ở chân."
    "Cô gái ngồi bên cạnh tủm tỉm cười với người bạn đẹp trai bên cạnh mình. Tay vuốt ve quyển sách như con thú cưng. "
    " Tôi cá là cô đang muốn cảm ơn anh chàng đẹp trai đã cứu mình."
    "Tôi không có tự nhận mình đẹp trai đâu nhé. Thế thì khoa trương quá! Không hợp với tính tôi đâu."
    "E hèm, trở lại vấn đề. Đứng trước mặt tôi đây là Azzurra Ines, cháu gái ông Tiziano Ines - một người hàng xóm trước đây của gia đình."
    "Bị cha mẹ bỏ rơi, cô phải dọn đến nhà ông mình là Tiziano. Từ đó, Azzurra không rời ông mình một giây nào."
    "Hoàn cảnh đáng thương như vậy, nên cô ấy luôn được mọi người chiếu cố. "
    "Cái tên Azzurra của cô có nghĩa là “xanh da trời”, nhưng tôi luôn gặp cô vào những lúc trời đỏ rực thế này. Kể có buồn cười không cơ chứ?"

    A"  Hết đau chưa?"
    show Azu P43_1 at center    
    AZ"  Chắc bầm một cục thôi."
    A"  Làm gì mà phải chạy thục mạng thế?"
    show Azu P7 at center
    AZ"  À thì là…"

    "Mặt Azzurra đỏ như gất. Cô khựng lại ở đó, không nói gì thêm."

    A"  Chậc. Sách mới nữa à?"

    "Thấy thế, tôi nhanh trí đánh trống lảng phá tan không khí bối rối."
    show Azu P17 at center
    AZ"  Ưm…"

    show black with dissolve
    show Azu_sp1 with dissolve3:
        yalign 0.008
        xalign 1.0
        linear 3.0 xalign 0.48

    show Azu_sp2 with dissolve3:
        yalign 0.5
        xalign 0.0
        linear 3.0 xalign 0.5

    show Azu_sp3 with dissolve3:
        yalign 0.992
        xalign 1.0
        linear 3.0 xalign 0.5
    $ renpy.pause(5.0)
    scene BG_6 :
        yalign 0.5
        xalign 0.5
        zoom 2.5
        linear 0.5 zoom 1.0
    show Azu P3 with dissolve2:
        yalign 0.99
        xalign 0.5
        zoom 2.5
        linear 0.5 zoom 1.0 
    "Azzurra không nói nhiều với người lạ, khả năng bắt chuyện của cô đương nhiên cũng thuộc hàng đội sổ. Vì thế cô không có nhiều bạn."
    "Từ ngày ông Ines mất, Azzurra chỉ sống một minh. Cũng nhờ đó, Azzurra tập giao tiếp nhiều hơn. "
    " Cha mẹ tôi – những người thường xuyên giúp đỡ Azzurra – cho rằng đây là một tín hiệu tốt."
    "Tuy nhiên, chỉ vài tháng sau, cô ấy lại đâm đầu vào những quyển sách. Suy cho cùng, cô ấy thế này, tôi cũng phải gánh một phần trách nhiệm."
    "Từ nhỏ, tôi đã rất thích những bí ẩn của thế giới, nhưng đọc sách một mình mới chán chết làm sao. "
    " May thay, Azzurra đã xuất hiện, cô ấy cũng có cùng hứng thú như tôi. Như đứa trẻ vớ được kẹo, tôi đã không ngần ngại đã lôi cô ấy vào chuyện này. "
    "Tất nhiên, một đứa trẻ không thể hiểu được mớ sách uyên bác của ông Ines, nên cha tôi đã nảy ra ý cho Azzurra mượn sách nhà mình. "
    " Vốn đã “luộc” qua mớ tài liệu đó từ lâu, nên tôi bất đắc dĩ đã trở thành bạn đồng hành của cô ấy. "
    " Khoảng cách của Azzurra và tôi từ đó thu hẹp lại dần."

    A"  Azu à, cậu phung phí tiền quá đấy!"

    "Tôi gằn giọng. Azzurra tròn mắt nhìn tôi một hồi lâu, rồi như đã nhận ra, bèn nhìn xuống quyển sách, cười trừ."
    show Azu P21 at center
    Az"  Nhưng nó hay mà!"

    "Thời gian trôi, mớ sách của gia đinh tôi hình như không còn đủ nữa. "
    " Nhưng sách của ông Ines thì vẫn còn quá cao siêu, thế nên mỗi tháng, một khoảng chi tiêu không nhỏ đã được cô ấy đốt vào kho sách của mình. "
    " Nghĩ lại thì, tôi có hơi hối hận. "

    show Azu P25 at center
    Az"  Mà này. Mình bảo cậu bao nhiêu lần rồi. Đừng gọi minh là Azu nữa rồi mà! Đồ Ana khùng!"
    A"  Hả? Chẳng phải cậu cũng gọi tớ bằng cái tên con gái đó đấy sao. "
    A" Tại mấy cậu mà tớ phải chết danh cái tên quỷ quái này rồi đấy. Còn nói nữa là tớ–"
    show Azu P29 at center
    Az"  “Tớ” sao?"

    "Azzurra hất tóc mái lên thách thức, hành động luôn được bắt gặp mỗi lần cô cắt lửng lời tôi như vậy."

    A"  Tớ bỏ về đấy!"
    show Azu P34 at center
    Az"  Thì cứ bỏ về đi. Ana khùng. Ana khùng Anaaaaaaaaaaaaaaa….Lêu lêu—"
    A"  Guaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

#//Màn hình lắc rung.
    with sshake
    "Nếu có lúc nào đó tôi muốn đòi đổi tên, thì đó là những lúc như thế này đây."

#oOo
#Cảnh: Đường phố
#Thời gian: Chiều
    scene BG_6 with dissolve
    stop music fadeout 1
    play music "Soundtracks/022 - Skipping.mp3" fadein 2.0
    "Thế quái nào, tôi lại quyết định ngồi đọc sách cùng Azzurra. Dù sao có người cãi lộn còn đỡ hơn nằm ườn như con lười ở nhà."

    A"  Tớ thua. Xin lỗi cậu. Làm ơn tha cho tớ."

    "Tôi xuống nước với cô. Dù gì có đứa dỗi thì phải có đứa dỗ thôi mà."

    show Azu P57 at center
    Az"  Từ nay còn dám gọi mình là Azu nữa không thôi?"
    A"  Dạ không ạ. “Chị hai” Azzurra."
    show Azu P22 at center
    Az" Haha. Thế có ngoan không?"

    "Cười gớm quá, Azzurra ạ!"

    A"  Không mượn cậu tấm tắc khen."
    A"  Thế quyển sách này ở đâu vậy?"

    "Nhìn nó giống một sách quý, khi được bọc lại rất cẩn thận."

    show Azu P27 at center
    Az"  Mình mua mà."
    A"  Nói dối. Tiền tiêu tháng này hết sạch còn đâu."

    "Nếu tôi nhớ không lầm, hôm qua, cô còn phải mượn tiền tôi. "

    show Azu P31 at center
    Az" ...."
    A"  Thế rốt cục là sách ở đâu ra? Đừng nói là hồi nãy cậu chạy đi cướp sách nhé."
    show Azu P59 at center
    Az"  Ứ-Ứ nói—"
    A"  Nói đi cho kẹo."
    show Azu P36 at center
    Az"  Đã bảo là không mà."
    A"  Tớ sẽ tò mò lắm đấy."
    show Azu P37 at center
    Az"  Kệ cậu."
    A"  Tớ sẽ lên máu vì hiếu kỳ."
    show Azu P34 at center
    Az"  Liên quan gì mình?"
    A"  Tớ sẽ chết không nhắm mắt."
    show Azu P33_1 at center
    Az" Ừ, bao giờ đám tang gọi mình."
    A"  ................."

    "Azzurra len lén nhìn qua tôi. Tôi cá rằng này giờ cô chẳng đọc được gì cả, chỉ làm màu thế."

    A"  Thế tớ về. Tạm biệt…"

    "Tôi phủi ống tay áo, giả vờ đứng dậy, chỉnh trang ghilê, cô vẫn cứng đầu làm ngơ tôi như vậy."
    "Mãi cho đến khi tôi giả vờ đi vài bước, Azzurra mới luống cuống kéo lại."

    show Azu P15_1 at center
    Az"   Ê nè nè. Đừng về! "

    "Biết tỏng mà. Cô nàng sẽ giữ tôi lại ngay thôi. "
    "Trong thế chứ nàng này hiền như cục đất, nãy giờ chẳng qua là cô được anh trai đẹp nhường ấy mà."
    
    A"  Vậy cậu nói đi."

#"Azzurra (tiu nghỉu): 

    show Azu P21 at center
    Az" Thực ra là..."

#//Hiệu ứng gợn sóng đồng tâm
#cảnh: công viên
#thời gian: chiều
    scene BG_6 with fade
    A"  Hả? "

#//Màn hình nẩy lên// 
    with sshake
    A" Cậu ăn trộm???"

    show Azu P15_1 at center
    Az"  Suỵt. Đừng nói khó nghe thế. Có phải mình cố ý ăn trộm đâu."
    A"  Nhưng rõ ràng cũng là ăn trộm mà."
    show Azu P16 at center
    Az"  Cũng đâu hẳn thế. Rõ ràng là ông chủ tiệm sách đánh rơi trước mà."
    show Azu P21 at center
    Az"  Mình không có ăn trộm mà, Anatolio…"
    "Azzurra báu vào tay áo tôi. Hóa ra con gái mè nheo cũng đau điếng tới vậy."
    A"  Hừm…"

    "Nói thể cũng không hẳn sai. Chuyện lão Ascenderos “sáu ngón” bất cẩn ném sách vung vãi giữa đường"
    " trong lúc sắp xếp từ cửa hàng sang nhà kho đối diện cũng bình thường thôi. "
    " Thật là, đã nghiện rượu, tay run thì cũng nên bớt keo kiệt mà bỏ tiền ra thuê người làm đi chứ nhỉ?"

#Thời gian: quá khứ
    scene BG_6 with fade
    show Azu P50 at center
    Az"  Đúng lúc đó mình đi ngang, thấy quyển sách đẹp quá nên mình lượm đại. Mãi một lúc ông chủ ra mình mới biết."

#Thời gian: chiều
    scene BG_6 with fade
    "Và thế là cậu ta “thó” luôn."
    "Người ta gọi đó là “bắt được của rơi, tạm thời bỏ túi” đấy."

    A"  Rồi, chú ấy đuổi theo cậu."
    show Azu P51 at center
    Az"  Không."
    A"  Thế cậu chạy làm gì?"
    show Azu P53 at center
    Az" Đề phòng."
    
    "Ai chứ ông chú Ascenderos, thú thật, chắc là lão cũng chẳng biết gì đâu. Chắc chỉ có cô nàng đại ngố này mới chạy thục mạng vì lão ta thôi."
    "Nhưng, nói gì thì nói..."

#//Màn hình nảy lên
    with sshake
    A"  Đó cũng là trộm. Trả sách cho người ta ngay đi!"
    show Azu P59 at center
    Az"  Không! Mình đang đọc mà."
    A"  Vậy đọc xong rồi trả."
    show Azu P59_1 at center
    Az"  Không! Mình phải đọc lại."
    A"  Thế rốt cục có trả không."
    show Azu P19 at center
    Az"  Nè. Cho cậu đấy."
    A"  Gì đây?"
    show Azu P12 at center
    Az"  Xem đi."

    "Azzurra bất chợt chìa một mảnh giấy. Mảnh giấy ố vàng được lấy từ trong quyển sách ra. "
    " Tuy vậy nét chữ trên đó vẫn còn in rõ ràng. Ngoại trừ một vài lỗ bị mọt gặm, tôi có thể nhận ra, đấy là một bài thơ tình:"

#Cảnh: đen

    scene black with dissolve

#//Hiện chữ trắng trên nền cảnh đen
#//NVL
    stop music fadeout 1
    play music "Soundtracks/016 - Winter when i can_t see you.mp3" fadein 2.0
    nvl_Center"“Loài phi yến vô hồn yếu ớt,"
    nvl_Center"Nàng đến đây, xích mạng sống của ta"
    nvl_Center"Đun cháy nó bằng lửa tình không ngớt,"
    nvl_Center"Của màu *** thuần khiết chẳng chút pha."
    nvl_Center"Nhìn kìa, cành phi yến thiết tha!"
    nvl_Center"Ta khiến nàng nở trong vườn ta đó!"
    nvl_Center"Ta nguyện dùng chính trái tim ta đỏ"
    nvl_Center"Xếp thành cành hoa, dâng tặng cho nàng."
    nvl_Center"Ôi, hỡi loài phi yến dịu dàng!"
    nvl_Center"Thân ta đây, lỗi vạn lần khó cãi."
    nvl_Center"Chỉ mong sao trong mối duyên lỡ mãi"
    nvl_Center"Hương sồi - hoa *** sẽ quyện hòa…
    "
    nvl clear
#------------------------------------------------
#******************”
#// Giovanni de’Rovere
#//tím
#Cảnh: công viên
#Thời gian: chiều
    stop music fadeout 1
    play music "Soundtracks/022 - Skipping.mp3" fadein 2.0
    scene BG_6 with dissolve

    show Azu P40 at center
    Az"Mình đoán nó phải là một bài thơ của một người thanh niên nghèo gửi tặng một công nương nào đấy. "
    A"Tớ lại thấy nó ghê ghê thế nào ấy."
    show Azu P39 at center
    Az"Anatolio đúng là chẳng có chút xíu tâm hồn văn thơ gì cả. "
    show Azu P42 at center
    Az" Rõ ràng là một bài thơ lãng mạn. Hoa phi yến này, lại còn hiến dâng tim nữa! Mình tững mối tình phân biệt giai cấp lắm. "
    show Azu P41 at center
    Az" Như Cô bé lọ lem này, Hoàng tử ếch này, và cả Don Quichotte nữa. Người nghèo mà giỏi giang thật hiếm thấy. "
    show Azu P40 at center
    Az"Không biết sau khi mình lớn lên có chàng bạch mã hoàng tử nào tặng cho mình trái tim không nhỉ?"

    " Tôi thắc mắc, có mối liên quan gì giữa mối tình phân biệt giai cấp và thằng hâm đi đánh cối xay không nhỉ?"

    A"Nè, đừng có nhìn tớ. Chắc chắn không phải tớ rồi."

#//Azzurra liếc

    A"Nè Azu. Lối suy nghĩ của cậu đúng là huyễn tưởng quá rồi đấy!"
    show Azu P26_1 at center
    Az"Huyễn tưởng chỗ nào?"
    A"Nói thật nhé. Tớ thấy cái cách xưng hô của nó giống như một kẻ hung bạo đầy quyền lực đang ép hôn cô gái hơn."
    A" Tớ không thấy chỗ nào gợi ý về một người nghèo cả."

    " Những động từ mạnh mẽ, kết hợp với hình ảnh máu me làm sống lưng tôi nhấp nhổm."

    show Azu P29 at center
    Az"Ừm. Cũng có lý. Đó cũng là một giả thuyết."
    A"Tớ lại chắc chắn như vậy đấy. Cậu không tin cũng đành chịu."
    show Azu P27 at center
    Az"Thế tóm lại là không phải một mối tình đẹp như tranh vẽ?"
    A"Không."
    show Azu P51 at center
    Az"Không phải mối tình của người thanh niên nghèo và một công chúa?"
    A"Chắc chắc không."

    " Azzurra mút ngón tay. Cô bạn tôi vẫn như thế mỗi lần cô ấy nhận ra điều gì ngớ ngẩn. "
    " Tôi ngửi mùi trên tờ giấy."

    A"Thậm chí nó còn không phải là thứ gì xa xưa. Chất giấy hơi vàng nhưng chắc chắn là giấy tốt. Lại còn cả con dấu này nữa."
    show Azu P52 at center
    Az"Ừ ha…"

    " Tuy được nhét trong quyển sách mục, tuổi giấy chắc chỉ độ chục có hơn. Con dấu bị mờ do thấm nước nhưng vẫn gợi cảm giác nửa quen nửa lạ."

    A"Mà này. Đừng có đánh trống lảng!"
    A"Chừng nào cậu mới định trả sách đây?"

    " Dù rằng tôi có thể phiên phiến cho qua và trả tiền hộ, nhưng tôi thực không muốn tạo tiền đề cho cô nàng phung phí. "
    " Phải rồi, cứ cho cô một bài học thì hơn."

    show Azu P59 at center
    Az"Mình không trả đâu. Ông ấy dữ lắm!"

    " Ra đây mới là lý do chính yếu."

    A" Không sao."
    A"Tớ sẽ đi với cậu!"
    show Azu P49 at center
    Az"Không! Không! Không! Không!"

#//Màn hình nảy lên.
    with sshake
    show Azu P31_1 at center
    Az"Mình đã giúp quyển sách này có chỗ sử dụng mà. Thế chẳng phải tốt hơn là kết cục nằm trong kho sao?"
    A"Cứu cánh không có biện minh được cho phương tiện đâu bé ạ. Trả sách cho người ta đi."
    show Azu P25 at center
    Az"Không nhé."
    A"Tớ sẽ dùng vũ lực đấy."
    show Azu P24 at center
    Az"Cứ việc nhé."
    A"Nào! Đưa đâyyy!!!!"

#//Màn hình rung lắc mạnh trong ít nhất 10s
    with sshake3
    show Azu P12 at center
    Az"Khônggggggggggggggggggggg!!!!!!"

    " Xem ra cô nhất quyết không chịu buông tay khỏi quyển sách."
    " Được rồi. Đã thế, tôi sẽ dùng tuyệt chiêu mới học được."
    " Hãy xem đây,..."

    return