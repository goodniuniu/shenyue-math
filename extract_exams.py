# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
import pdfplumber

SRC = Path("知识库/数学/素材与拓展/真题试卷")
OUT = SRC / "提取文本"
OUT.mkdir(exist_ok=True)
for pdf_path in sorted(SRC.glob("*.pdf")):
    texts = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for i, page in enumerate(pdf.pages):
            t = page.extract_text() or ""
            texts.append(f"--- page {i+1} ---\n" + t)
    out = OUT / (pdf_path.stem + ".txt")
    out.write_text("\n".join(texts), encoding="utf-8")
    print(pdf_path.name, "->", sum(len(t) for t in texts), "chars")
