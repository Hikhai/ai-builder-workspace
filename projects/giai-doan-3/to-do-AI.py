import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

def tinh_ngay(so_ngay):
    ket_qua = datetime.now() + timedelta(days=so_ngay)
    thu_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
    ngay_thang = ket_qua.strftime("%d/%m/%Y")
    thu = thu_trong_tuan[ket_qua.weekday()]
    return f"{ngay_thang} ({thu})"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "tinh_ngay",
            "description": "Tính ra ngày và thứ trong tuần cụ thể (dd/mm/yyyy) bằng cách cộng thêm 1 số ngày vào ngày hôm nay. Dùng hàm này bất cứ khi nào cần tính một ngày trong tương lai, không tự đoán bằng lời.",
            "parameters": {
                "type": "object",
                "properties": {
                    "so_ngay": {
                        "type": "integer",
                        "description": "Số ngày cần cộng thêm vào hôm nay để ra ngày đích"
                    }
                },
                "required": ["so_ngay"],
            },
        },
    }
]

def hoi(cau_hoi, toi_da_vong_lap=5):
    messages = [
        {"role": "system", "content": f"Hôm nay là {datetime.now().strftime('%d/%m/%Y')}."},
        {"role": "user", "content": cau_hoi},
    ]

    for _ in range(toi_da_vong_lap):
        response = client.chat.completions.create(model="openrouter/free", messages=messages, tools=TOOLS)
        tin_nhan = response.choices[0].message

        if not tin_nhan.tool_calls:
            return tin_nhan.content

        messages.append(tin_nhan)
        for goi_ham in tin_nhan.tool_calls:
            print(f"[Model yêu cầu gọi: {goi_ham.function.name}({goi_ham.function.arguments})]")
            tham_so = json.loads(goi_ham.function.arguments)
            ket_qua = tinh_ngay(tham_so["so_ngay"])
            print(f"[Kết quả thật từ hàm: {ket_qua}]")   # <-- MỚI: in raw kết quả để đối chiếu
            messages.append({"role": "tool", "tool_call_id": goi_ham.id, "content": ket_qua})

    return "Không trả lời được sau nhiều lượt gọi hàm."

if __name__ == "__main__":
    print(hoi(input("Câu hỏi: ")))