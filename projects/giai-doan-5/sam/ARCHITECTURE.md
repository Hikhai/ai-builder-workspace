# ARCHITECTURE - SAM

## Kiến trúc tổng thể
- Layer presentation: frontend React
- Layer API: FastAPI routers và dependency injection
- Layer business: capabilities / flows
- Layer data: SQLAlchemy models và database session
- Layer AI: tool functions gọi LLM

## Thành phần chính
- app/main.py: điểm khởi động FastAPI
- app/core/config.py: cấu hình environment
- app/core/database.py: engine/session/Base
- app/models: các model dữ liệu
- app/routers: định nghĩa API endpoint
- app/capabilities: luồng nghiệp vụ cao cấp
- app/tools: các helper gọi LLM
