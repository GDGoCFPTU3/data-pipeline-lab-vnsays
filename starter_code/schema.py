from pydantic import BaseModel
from typing import Optional

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hợp đồng dữ liệu chuẩn cho toàn bộ pipeline.
    Cả PDF lẫn Video đều phải map vào schema này.
    """
    document_id: str
    source_type: str
    author: Optional[str] = "Unknown"
    category: str
    content: str
    timestamp: str
