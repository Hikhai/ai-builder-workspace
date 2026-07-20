import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[{"role": "user", "content": """Bản Giao Hưởng Của Mùa Thu
        Mùa thu luôn mang đến cho con người những cảm xúc khó tả, một sự pha trộn tinh tế giữa vẻ đẹp tĩnh lặng và những hoài niệm miên man. Khi tia nắng gay gắt của mùa hè dần lùi bước, nhường chỗ cho từng đợt gió heo may lướt qua tán lá, đó là lúc ta nhận ra nàng thu đã khẽ khàng gõ cửa. Bầu trời như vừa được gội rửa, khoác lên mình màu xanh trong vắt, cao vời vợi và tuyệt nhiên không một gợn mây xám xịt. Không khí buổi sáng sớm mang theo cái se lạnh nhè nhẹ, đủ để khiến người ta khẽ rùng mình khoác thêm chiếc áo mỏng, nhưng cũng đủ sức xua tan đi bao ồn ào, ngột ngạt của cuộc sống thường nhật.

        Bước dạo quanh những con phố quen thuộc, ta dễ dàng bắt gặp những hình ảnh bình dị mà vô cùng đậm chất thơ. Hàng cây cổ thụ bên đường bắt đầu chuyển mình, điểm xuyết những chiếc lá vàng, lá đỏ rực rỡ giữa nền xanh mướt của thiên nhiên. Mỗi cơn gió lạnh thoảng qua, từng chiếc lá lại khẽ khàng lìa cành, chao nghiêng xoay vòng trong không trung như những vũ công đang say sưa biểu diễn điệu múa cuối cùng. Tiếng lá khô xào xạc dưới mỗi bước chân tạo nên một bản nhạc êm ái, như đang thì thầm kể câu chuyện muôn thuở về thời gian và sự luân hồi của vạn vật.

        Khắp các nẻo đường, mùi hương hoa sữa thoang thoảng len lỏi vào từng ngóc ngách, gợi nhắc lại bao kỷ niệm xưa cũ. Hương thơm ấy không hề nồng nàn mà dịu nhẹ, e ấp nhưng lại có sức vương vấn đến kỳ lạ. Nó khiến những tâm hồn đang vội vã chạy theo guồng quay của công việc bỗng chốc muốn chậm lại một nhịp, hít một hơi thật sâu để tận hưởng trọn vẹn món quà mà thiên nhiên ban tặng. Nhâm nhi một tách cà phê nóng bên góc quán nhỏ, ngắm nhìn dòng người tấp nập qua lại, ta bỗng thấy lòng mình bình yên lạ thường, dường như mọi âu lo đều tan biến theo cơn gió.

        Mùa thu không chỉ đẹp bởi cảnh sắc mà còn bởi những giá trị tinh thần to lớn nó mang lại. Đây là mùa của sự đoàn viên, của chiếc đèn ông sao rực rỡ sắc màu, hương vị bánh nướng bánh dẻo ngọt ngào và tiếng cười rạng rỡ của trẻ thơ. Đó cũng là lúc con người ta muốn quay về với thế giới nội tâm, suy ngẫm về những gì đã qua và nuôi dưỡng những hy vọng tốt đẹp cho tương lai. Dù cuộc sống có bận rộn đến mấy, hãy dành ra những khoảnh khắc tĩnh lặng để cảm nhận vẻ đẹp diệu kỳ của đất trời.

        Mỗi khoảnh khắc trôi qua đều là duy nhất và không bao giờ lặp lại. Khi biết lắng nghe nhịp đập của thiên nhiên, ta sẽ tìm thấy sự cân bằng, thanh thản trong chính tâm hồn mình. Mùa thu cứ thế trôi đi một cách êm đềm, để lại trong tâm trí mỗi chúng ta những dấu ấn khó phai, tựa như một bức tranh tuyệt mỹ được vẽ bởi bàn tay tạo hóa, nhắc nhở chúng ta về ý nghĩa bình dị mà sâu sắc của cuộc đời. Hãy trân trọng hiện tại, yêu thương bản thân và lan tỏa sự ấm áp đến với mọi người xung quanh trong những ngày thu tuyệt đẹp này."""}],
        )

print(response.choices[0].message.content)
print(response.usage)