# 📚 Vocabulary Practice API Workshop

> **FastAPI + MySQL + Docker Workshop Template**
> เรียนรู้การสร้าง REST API พร้อม Database และ Frontend Integration ในเวลา 1 ชั่วโมง

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-000000?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

## 📖 เกี่ยวกับ Workshop

Workshop นี้ออกแบบมาเพื่อสอนนักศึกษาสร้างแอปพลิเคชันฝึกภาษาอังกฤษแบบ Full-Stack โดยใช้เทคโนโลยีที่ทันสมัย เหมาะสำหรับนักศึกษาที่กำลังทำ **Term Project** เกี่ยวกับ Vocabulary Learning, Language Practice, หรือโปรเจคที่ต้องการ:

- ✅ REST API Backend
- ✅ Database Integration (MySQL)
- ✅ Frontend-Backend Connection
- ✅ Data Visualization
- ✅ AI/Mock Validation System

### 🎯 สิ่งที่จะได้เรียนรู้

- **FastAPI**: สร้าง RESTful API ที่เร็วและมี auto-documentation
- **MySQL + Docker**: จัดการ database ด้วย Docker Compose
- **SQLAlchemy ORM**: เชื่อมต่อและจัดการข้อมูลแบบ Object-Oriented
- **Next.js + React**: สร้าง modern frontend ด้วย TypeScript
- **API Integration**: เชื่อมต่อ Frontend-Backend อย่างถูกต้อง
- **Data Visualization**: สร้างกราฟด้วย Recharts
- **Mock AI System**: เตรียมพร้อมสำหรับ real AI integration (n8n/OpenAI)

---

## 🚀 Quick Start

### Prerequisites

ก่อนเริ่ม Workshop ต้องติดตั้งโปรแกรมเหล่านี้:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (รวม Docker Compose)
- [Node.js](https://nodejs.org/) version 18 หรือสูงกว่า
- [Git](https://git-scm.com/)
- Code Editor (แนะนำ [VS Code](https://code.visualstudio.com/))

### ⚡ เริ่มต้นใช้งาน (5 นาที)

**1. Clone Repository**
```bash
git clone https://github.com/your-username/vocabulary-api-workshop.git
cd vocabulary-api-workshop
```

**2. เริ่ม Backend + Database**
```bash
docker-compose up -d
```

รอ Docker ทำงาน:
- 🗄️ สร้าง MySQL container
- 📋 Run `init.sql` สร้างตารางและข้อมูลตัวอย่าง
- 🚀 Start FastAPI server

**3. ตรวจสอบ API**

เปิด browser ไปที่ http://localhost:8000/docs

คุณจะเห็น **Swagger UI** สำหรับทดสอบ API ทันที!


---

## 📁 โครงสร้างโปรเจค
```
vocabulary-api-workshop/
│
├── 📂 api/                   # FastAPI Backend
│   ├── main.py               # API endpoints หลัก
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Backend container config
│
│
├── docker-compose.yml        # Docker orchestration
├── init.sql                  # Database schema & seed data
└── README.md                 # คุณกำลังอ่านอยู่! 👋
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | API information | JSON with endpoints list |
| `GET` | `/api/word` | สุ่มคำศัพท์ 1 คำ | Word object |
| `POST` | `/api/validate-sentence` | ตรวจประโยค + ให้คะแนน | Validation result |
| `GET` | `/api/summary` | สถิติการฝึกทั้งหมด | Summary statistics |
| `GET` | `/api/history` | ประวัติการฝึก | Array of practice sessions |
| `GET` | `/health` | Health check | Status object |

### 📝 ตัวอย่างการใช้งาน

#### 1. ดึงคำศัพท์สุ่ม

**Request:**
```bash
curl http://localhost:8000/api/word
```

**Response:**
```json
{
  "id": 1,
  "word": "apple",
  "definition": "A round fruit with red, green, or yellow skin",
  "difficulty_level": "Beginner"
}
```

#### 2. ส่งประโยคเพื่อตรวจสอบ

**Request:**
```bash
curl -X POST http://localhost:8000/api/validate-sentence \
  -H "Content-Type: application/json" \
  -d '{
    "word_id": 1,
    "sentence": "I eat an apple every morning for breakfast"
  }'
```

**Response:**
```json
{
  "score": 8.5,
  "level": "Beginner",
  "suggestion": "Excellent! Your sentence is well-structured and descriptive.",
  "corrected_sentence": "I eat an apple every morning for breakfast"
}
```

#### 3. ดูสถิติการฝึก

**Request:**
```bash
curl http://localhost:8000/api/summary
```

**Response:**
```json
{
  "total_practices": 15,
  "average_score": 7.8,
  "total_words_practiced": 5,
  "level_distribution": {
    "Beginner": 8,
    "Intermediate": 5,
    "Advanced": 2
  }
}
```

---

## 🗄️ Database Schema

### Table: `words`

เก็บคำศัพท์ทั้งหมดในระบบ

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INT | PRIMARY KEY, AUTO_INCREMENT | รหัสคำศัพท์ |
| `word` | VARCHAR(100) | UNIQUE, NOT NULL | คำศัพท์ภาษาอังกฤษ |
| `definition` | TEXT | | ความหมาย/คำจำกัดความ |
| `difficulty_level` | ENUM | 'Beginner', 'Intermediate', 'Advanced' | ระดับความยาก |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | วันที่เพิ่มคำศัพท์ |

### Table: `practice_sessions`

เก็บประวัติการฝึกของผู้ใช้

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INT | PRIMARY KEY, AUTO_INCREMENT | รหัสการฝึก |
| `word_id` | INT | FOREIGN KEY → words(id) | คำศัพท์ที่ฝึก |
| `user_sentence` | TEXT | NOT NULL | ประโยคที่ผู้ใช้แต่ง |
| `score` | DECIMAL(3,1) | | คะแนน (0.0-10.0) |
| `feedback` | TEXT | | คำแนะนำจาก AI |
| `corrected_sentence` | TEXT | | ประโยคที่แก้ไขแล้ว |
| `practiced_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | วันเวลาที่ฝึก |

### ER Diagram
```
┌─────────────┐         ┌───────────────────┐
│   words     │         │ practice_sessions │
├─────────────┤         ├───────────────────┤
│ id (PK)     │◄────────│ id (PK)           │
│ word        │    1:N  │ word_id (FK)      │
│ definition  │         │ user_sentence     │
│ difficulty  │         │ score             │
│ created_at  │         │ feedback          │
└─────────────┘         │ corrected_sentence│
                        │ practiced_at      │
                        └───────────────────┘
```

---

## 🎨 Frontend Features

### 1. 🎯 Word Challenge Page (`/`)

หน้าหลักสำหรับฝึกแต่งประโยค

**Features:**
- แสดงคำศัพท์แบบสุ่มพร้อมความหมาย
- แสดง difficulty level (Beginner/Intermediate/Advanced)
- Form สำหรับพิมพ์ประโยค
- Real-time validation & scoring
- ระบบสีตามคะแนน:
  - 🟢 เขียว: คะแนน ≥ 8.0
  - 🟡 เหลือง: คะแนน 6.0-7.9
  - 🔴 แดง: คะแนน < 6.0
- ปุ่มข้ามคำ และลองคำใหม่

### 2. 📊 Dashboard Page (`/dashboard`)

หน้าแสดงสถิติและผลการฝึก

**Features:**
- **Stats Cards**: 
  - จำนวนครั้งที่ฝึกทั้งหมด
  - คะแนนเฉลี่ย
  - จำนวนคำศัพท์ที่ฝึกแล้ว
- **Bar Chart**: แสดงการกระจายของการฝึกแยกตาม difficulty level
- **Recent History**: แสดง 5 รายการล่าสุด พร้อมคะแนนและ feedback
- Responsive design ใช้งานได้ทั้ง desktop และ mobile

---

## 🛠️ Development Guide

### การจัดการ Docker Containers

**ดูสถานะ containers:**
```bash
docker ps
```

**Restart services:**
```bash
# Restart ทั้งหมด
docker-compose restart

# Restart เฉพาะ FastAPI
docker-compose restart fastapi

# Restart เฉพาะ MySQL
docker-compose restart mysql
```

**ดู logs:**
```bash
# Logs ทั้งหมด
docker-compose logs -f

# Logs เฉพาะ service
docker-compose logs -f fastapi
docker-compose logs -f mysql
```

**หยุด containers:**
```bash
docker-compose down
```

**ลบข้อมูลและเริ่มใหม่:**
```bash
docker-compose down -v  # ลบ volumes (ข้อมูลใน database จะหายด้วย)
docker-compose up -d
```

### การจัดการ Database

**เข้าใช้งาน MySQL CLI:**
```bash
docker exec -it vocab_mysql mysql -u vocabuser -pvocabpass123 vocabulary_db
```

**เพิ่มคำศัพท์ใหม่:**
```sql
INSERT INTO words (word, definition, difficulty_level) VALUES 
('courage', 'The ability to do something frightening', 'Intermediate'),
('serendipity', 'Finding something good without looking for it', 'Advanced');
```

**ดูข้อมูลทั้งหมด:**
```sql
-- ดูคำศัพท์ทั้งหมด
SELECT * FROM words;

-- ดูประวัติการฝึก 10 รายการล่าสุด
SELECT * FROM practice_sessions ORDER BY practiced_at DESC LIMIT 10;

-- ดูสถิติ
SELECT 
  difficulty_level,
  COUNT(*) as total_practices,
  AVG(score) as avg_score
FROM practice_sessions ps
JOIN words w ON ps.word_id = w.id
GROUP BY difficulty_level;
```

**Export ข้อมูล:**
```bash
docker exec vocab_mysql mysqldump -u vocabuser -pvocabpass123 vocabulary_db > backup.sql
```

**Import ข้อมูล:**
```bash
docker exec -i vocab_mysql mysql -u vocabuser -pvocabpass123 vocabulary_db < backup.sql
```
## 🎓 Workshop Timeline

**ระยะเวลา: 1 ชั่วโมง**

| เวลา | หัวข้อ | กิจกรรม | เป้าหมาย |
|------|--------|---------|----------|
| - | 🎬 Introduction & Setup | - Clone repository<br>- `docker-compose up`<br>- ทดสอบ API docs | นักศึกษาเห็น environment ที่พร้อมใช้งาน |
| - | 🐳 Docker & Database | - อธิบาย `docker-compose.yml`<br>- อธิบาย `init.sql`<br>- ทดสอบ MySQL | เข้าใจ Docker architecture |
| - | ⚡ FastAPI Backend | - Code along: `main.py`<br>- สร้าง 4 endpoints<br>- ทดสอบใน Swagger UI | เข้าใจ REST API & Database ORM |
| - | ⚛️ Next.js Frontend | - สร้าง Word Challenge page<br>- สร้าง Dashboard<br>- เชื่อมต่อ API | เข้าใจ Frontend-Backend integration |
| - | ✅ Testing & Demo | - ทดสอบ full flow<br>- แก้ bugs ถ้ามี | นักศึกษามี working application |
| - | 💡 Q&A & Next Steps | - ตอบคำถาม<br>- แนะนำการพัฒนาต่อ | แนวทางสำหรับ term project |

---

## 🚀 แนะนำการพัฒนาต่อ (สำหรับ Term Project)

### 🤖 1. เชื่อมต่อ AI จริง (n8n + OpenAI)

แทนที่ `mock_ai_validation()`:
```python
import requests

def ai_validation_with_n8n(sentence: str, word: str, level: str):
    """เรียก n8n webhook ที่เชื่อม OpenAI"""
    response = requests.post(
        "https://your-n8n-instance.com/webhook/validate",
        json={
            "sentence": sentence,
            "target_word": word,
            "difficulty": level
        },
        timeout=10
    )
    return response.json()
```

**n8n Workflow แนะนำ:**
1. Webhook Trigger
2. OpenAI Node (GPT-4)
   - Prompt: "Evaluate this English sentence..."
3. Return JSON response

### 🎮 2. Gamification Features

**Streak System:**
```python
# เพิ่ม table
CREATE TABLE user_streaks (
    user_id INT,
    current_streak INT DEFAULT 0,
    longest_streak INT DEFAULT 0,
    last_practice_date DATE
);
```

**Achievement System:**
```python
achievements = {
    "first_practice": "แต่งประโยคครั้งแรก",
    "score_perfect": "คะแนนเต็ม 10/10",
    "streak_7": "ฝึกติดต่อกัน 7 วัน",
    "words_50": "ฝึก 50 คำศัพท์แล้ว"
}
```

### 📱 3. Advanced Features
**Image Integration (Unsplash API):**
```python
@app.get("/api/word/{word_id}/image")
def get_word_image(word_id: int):
    word = db.query(Word).filter(Word.id == word_id).first()

    response = requests.get(
        f"https://api.unsplash.com/search/photos?query={word.word}",
        headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"}
    )
    return response.json()
```

**Export Progress (PDF):**
```python
from reportlab.pdfgen import canvas

@app.get("/api/export/pdf")
def export_progress_pdf(user_id: int):
    # สร้าง PDF report ของผู้ใช้
    pass
```

## 📚 Learning Resources

### Official Documentation
- 📘 [FastAPI Documentation](https://fastapi.tiangolo.com/) - Complete guide
- 📘 [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- 📘 [Docker Compose Reference](https://docs.docker.com/compose/)
- 📘 [Next.js App Router](https://nextjs.org/docs/app)

### Video Tutorials
- 🎥 [FastAPI Crash Course](https://www.youtube.com/results?search_query=fastapi+tutorial)
- 🎥 [Docker for Beginners](https://www.youtube.com/results?search_query=docker+tutorial)

### Related Projects & Inspiration
- [speechful](https://www.speechful.ai/) - Achieve your target IELTS score with Speechful
- [Duolingo](https://www.duolingo.com/) - Language learning gamification
- [Anki](https://apps.ankiweb.net/) - Spaced repetition flashcards
- [Quizlet](https://quizlet.com/) - Study tools and flashcards


---

<div align="center">

**Made with ❤️ and ☕️ for Learner**
[⬆ กลับไปด้านบน](#-vocabulary-practice-api-workshop)
</div>