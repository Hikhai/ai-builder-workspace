import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

HOM_NAY = datetime.now().strftime("%d/%m/%Y")

SYSTEM_PROMPT = f"""Bạn là công cụ trích xuất dữ liệu công việc từ câu tiếng Việt tự nhiên.
Hôm nay là ngày {HOM_NAY}.
Chỉ trả về đúng 1 đối tượng JSON, không giải thích, không thêm chữ nào khác ngoài JSON.
JSON có đúng 3 trường: "ten_cong_viec" (chuỗi ngắn gọn), "do_quan_trong" (chỉ "Gấp" hoặc "Không gấp"), "han_deadline" (định dạng dd/mm/yyyy).

Ví dụ:
Input: "Mai phải nộp bài tập môn Toán, hơi gấp"
Output: {{"ten_cong_viec": "Nộp bài tập môn Toán", "do_quan_trong": "Gấp", "han_deadline": "21/07/2026"}}

Input: "Cuối tháng sau nhớ đi khám sức khỏe định kỳ"
Output: {{"ten_cong_viec": "Đi khám sức khỏe định kỳ", "do_quan_trong": "Không gấp", "han_deadline": "31/08/2026"}}
"""

def trich_xuat(cau_noi):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": cau_noi},
        ],
    )
    noi_dung = response.choices[0].message.content
    try:
        return json.loads(noi_dung)
    except json.JSONDecodeError:
        print(f"Model trả về không đúng JSON:\n{noi_dung}")
        return None

if __name__ == "__main__":
    cac_cau_test = [
        "Nhắc tôi nộp báo cáo tuần trước thứ 6 tuần sau, gấp lắm",
        "Tuần sau đi sinh nhật bạn thân, không gấp lắm",
    ]
    for cau in cac_cau_test:
        ket_qua = trich_xuat(cau)
        print(f"Input: {cau}")
        print(f"Output: {ket_qua}\n")