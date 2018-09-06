label Escape_E002_E001_C002_E001_E001_E002_E:
    $ Sys_GameProgress = "Escape_E002_E001_C002_E001_E001_E002"
    if Sys_SkipAll > 0:
        stop music fadeout 1.0
        play music "Soundtracks/015 - Dying World.mp3" fadein 1.0
        " Nói rồi Azzurra im lặng. Azzurra nhắm mắt lại, ngồi phịch xuống chiếc ghế cạnh bàn."

        A"   Cậu làm sao vậy? Azzurra?"
        show Azu P50 at center
        Az"  Mình xin lỗi. Mình.... muốn nghỉ một lúc."

        "Azzurra gục mặt xuống bàn, dường như không còn đủ năng lượng để làm gì nữa."
        hide Azu P50
        show Azu Fredo P0 at center
        F"   Ta nghĩ rằng con nên để Azzurra ở lại đây."
        A"   Để Azzurra? Ở lại với Cha sao?"
        show Azu Fredo P1 at center
        F"   Con không tin ta, đứng không?"

        " Phải. Tôi không nghĩ rằng trong vài tháng – hoặc thậm chí vài năm – nữa cha Fredo có thể khả dĩ giành lại lòng tin của tôi."

        A"   Con rất lấy làm tiếc."
        show Azu Fredo P2 at center
        F"   Ta hiểu."
        show Azu Fredo P3 at center
        F"   Ta chỉ mong con hãy suy nghĩ cho sáng một chút. Bây giờ con định đưa Azzurra đi đâu?"
        A"   …"
        show Azu Fredo P0 at center
        F"   Về nhà, đúng không?"
        A"   Còn chỗ nào khác nữa, thưa Cha?"
        show Azu Fredo P2 at center
        F"   Nhà con không an toàn như con tưởng đâu."

        " Tôi giật mình đánh thót."

        A"   Ý... ý Cha là gì?"
        show Azu Fredo P3 at center
        F"   Con đủ thông minh để hiểu, đúng không? Con nghĩ vô tình mà con biết được Azzurra đang ở đâu à? "
        show Azu Fredo P0 at center
        F"  Con nghĩ vô tình mà con được tiếp cận với những nguồn thông tin mà cách đây một thế hệ Giáo hội sẵn sàng tiêu diệt những kẻ nắm chúng – "
        show Azu Fredo P2 at center
        F"  vô tình hoặc hữu ý – à?."

        " Tôi trợn tròn hai mắt. Chẳng lẽ Cha biết về ông Attenborough? Không thể nào!"
        " Không, có thể chứ!"

        show Azu Fredo P0 at center
        F"   Ta sẽ thận trọng hơn nếu ta là con."
        A"   Nhưng... nhưng làm sao con tin rằng..."
        show Azu Fredo P2 at center
        F"   Con nghĩ rằng ta sẽ làm hại Azzurra sao?"
        A"   Nhưng Hanes..."
        show Azu Fredo P1 at center
        F"   Hãy nhớ rằng ta là bạn của Ines từ trước khi con sinh ra. Cháu nuôi của Ines là cháu ta."
        A"   Nhưng Hanes là cháu ruột của Cha, phải không? Làm sao con tin được rằng Cha sẽ bảo vệ Azzurra nếu như..."
        show Azu Fredo P3 at center
        F"   Bởi vì ta không muốn Hanes đi theo con đường nó muốn đi."
        A"   Thế còn chính Cha thì sao? Cha sẽ không vì Azzurra mà đưa chính mình vào rắc rối với Giáo hội, phải không Cha?"
        show Azu Fredo P0 at center
        F"   ..."
        A"   Cha không trả lời được, đúng không?"

        " Bỗng cha Fredo bật cười."

        A"   Thưa Cha?"
        show Azu Fredo P0 at center
        F"   Anatolio Pietro, con đánh giá ta hơi thấp. "
        show Azu Fredo P2 at center
        F"  Chẳng lẽ ta sống từng ấy năm, trải qua những thử thách khiến Giáo hoàng cũng phải ngại, mà không có lấy một ít vốn để tự vệ sao?"

        " Bây giờ tới lượt tôi đớ người."
        " Cha đặt tay lên vai tôi rồi gật đầu."

        show Azu Fredo P3 at center
        F"   Hãy tin ở ta. Để Azzurra ở lại đây đi."

        " Tôi không biết tôi đang nghĩ gì nữa, nhưng bỗng nhên lúc ấy, hình ảnh một cha Fredo thân thiện, tốt bụng và hiền từ – "
        " ông thánh sống trong lòng lũ nhỏ chúng tôi – đã hồi sinh."
        " Có thể tôi đang hóa điên, nhưng... tôi cảm thấy tôi có thể tin được Cha."
        " Hoặc cũng có thể tôi đang lo cho chính mình và chính gia đình mình. Tôi không biết cuối cùng lý do của tôi là gì nữa.'"
        " Chỉ có quyết định của tôi là quan trọng thôi."

        A"   Nếu đã vậy thì... trăm sự nhờ Cha."

        " Tôi bỏ thõng hai tay xuống."

        A"   Cha... đừng làm con phải hối hận. Xin Cha."
        show Azu Fredo P3 at center
        F"   Con yên tâm."
        show Azu Fredo P0 at center
        F"   Thôi, con đi được rồi đấy. Chỗ này không ở lâu được."

        " Cha gật đầu."

        show Azu Fredo P2 at center
        F"   Các vị thiên thần che chở cho con."

    $ Azzurra_Stays_With_Fredo = 1

    return