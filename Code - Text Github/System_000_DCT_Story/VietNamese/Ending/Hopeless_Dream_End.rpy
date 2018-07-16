label Hopeless_Dream_End:

#Cảnh: Anatolio (Về già), ngồi dưới gốc cây cổ thụ trên một chiếc xe lăn, nhìn lên bầu trởi đầy sao.
#//NVL
    stop music fadeout 1.0
    play music "Soundtracks/Demo2_3.mp3" fadein 1.0
    scene BG_5 with fade
    nvlDC"Phải, tôi đã mong muốn đó chỉ là tạm biệt."
    nvlDC"\n Nhưng sau đó, tôi không bao giờ còn gặp lại Azzurra nữa."
    nvlDC"\n Sau Lễ hội Mặt trời, nhóm Schallendorf cũng rời khỏi ngôi nhà lợp ngói ấy, mang theo cả Azzurra."
    nvlDC"\n Ông Attenborough cũng không đến tìm tôi nữa, nhận ra rằng, xét cho cùng, tôi đã thất bại. Dù là ai, là tổ chức nào đi nữa, họ cũng không cần một kẻ thất bại."
    nvlDC"\n Tôi cũng không biết kết quả của cuộc phiêu lưu của nhóm Schallendorf trong những nghiên cứu của họ như thế nào; liệu họ có thoát khỏi thế giới tí hon của chúng tôi hay không."
    nvlDC"\n Tôi chỉ biết rằng trong nửa thế kỷ còn lại của cuộc đời tôi, quyền lực của Giáo hội vẫn là tối thượng. Nếu có một thế giới ngoài kia, thế giới ấy vĩnh viễn nằm ngoài tầm với của chúng tôi."
    nvlDC"\n Cho tới phút này đây, khi cuộc đời tôi có lẽ chỉ tính bằng tháng, tôi vẫn ngồi đó, dưới gốc cây, trên chiếc xe lăn, nhìn lên bầu trời kia, tôi vẫn không hiểu liệu mình đã lựa chọn đúng hay chưa."
    nvlDC"\n Có lẽ trong nhiều kiếp đầu thai nữa, tôi sẽ vẫn mãi hối hận quyết định của mình."
    nvlDC"\n Trên vòm trời kia, đường chân trời vẫn ngự trị, như đang cười mỉa mai trước những cố gắng vô vọng của những con người nhỏ nhoi vẫn cố gắng vươn ra ngoài nó mà không thoát ra được khỏi giới hạn của chính mình.
    "
    nvl clear

#Cảnh: Bầu trời sao

    A" Bởi vì... con người luôn luôn vươn tới những gì không thể đạt được."
    $ show_quick_menu1 = False
    show fin_white:
     yalign 0
     xalign 0.9
     alpha 0
     linear 2 alpha 1
    $renpy.pause (2)
    hide fin_white 

    return