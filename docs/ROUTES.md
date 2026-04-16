# 路由與頁面設計文件 (ROUTES)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 | GET | `/` | `index.html` | 顯示首頁，包含排行榜摘要與新書區 |
| 書籍列表 / 搜尋 | GET | `/books` | `books/list.html` | 列出所有書籍，並可接收搜尋關鍵字查詢 |
| 新增書籍頁面 | GET | `/books/new` | `books/create.html` | 顯示新增表單 |
| 建立書籍 | POST | `/books` | — | 接收書籍表單，存入 DB，重導向到詳情頁 |
| 書籍詳情 | GET | `/books/<id>` | `books/detail.html` | 顯示書籍詳情、心得清單、留言列表 |
| 編輯書籍頁面 | GET | `/books/<id>/edit` | `books/edit.html` | 顯示編輯表單，預填現有資料 |
| 更新書籍 | POST | `/books/<id>/update` | — | 更新書籍資料，重導向至詳情頁 |
| 刪除書籍 | POST | `/books/<id>/delete` | — | 刪除書籍並重導向回列表頁 |
| 建立心得評分 | POST | `/reviews/<book_id>` | — | 接收評分及心得內容，重導向至書籍詳情頁 |
| 建立留言/回覆 | POST | `/comments/<book_id>`| — | 接收留言內容（含可選的回覆 `parent_id`），重導向至詳情頁 |
| 排行榜 | GET | `/ranking` | `ranking.html` | 顯示評分最高的前幾名書籍 |
| 本月新書 | GET | `/new-books` | `new_books.html` | 顯示本月份新增的書籍 |

## 2. 路由詳細說明

### 2.1 首頁路由 (`app/routes/main.py`)
- **GET `/`**
  - 輸入：無
  - 邏輯：從 DB 抓取幾筆評分最高的書籍作為推薦、以及近期建立的書籍做展示。
  - 輸出：渲染 `index.html`。

### 2.2 書籍路由 (`app/routes/books.py`)
- **GET `/books`**
  - 輸入：URL Query Parameter（如 `?q=關鍵字`）。
  - 邏輯：有 `q` 時以模糊搜尋比對書名與作者；否則抓取全部。
  - 輸出：渲染 `books/list.html`。
- **GET `/books/new`**
  - 輸入：無
  - 邏輯：準備空表單給使用者。
  - 輸出：渲染 `books/create.html`。
- **POST `/books`**
  - 輸入：表單（標題、作者、出版社、日期、ISBN）。
  - 邏輯：資料驗證，若成功則 `Book.create(...)` 並重導向到新建立的詳情頁。
  - 錯誤：驗證失敗的話重新渲染 `books/create.html` 並帶入錯誤訊息。
- **GET `/books/<id>`**
  - 輸入：書籍 id。
  - 邏輯：從 DB 取得對應 `Book` 及所有關聯 `Review` 與 `Comment`。
  - 輸出：若是 404，回傳 NotFound；否則渲染 `books/detail.html`。
- **GET `/books/<id>/edit`**
  - 輸入：書籍 id。
  - 邏輯：抓取指定 `Book` 資料來預填。
  - 輸出：渲染 `books/edit.html`。
- **POST `/books/<id>/update`**
  - 輸入：書籍 id 與表單資料。
  - 邏輯：更新書籍與 DB，並重導向回詳情頁。
- **POST `/books/<id>/delete`**
  - 輸入：書籍 id。
  - 邏輯：將書籍刪除（Cascade 將連帶刪除心得與留言），並重導向至書籍列表 `/books`。

### 2.3 心得與評分路由 (`app/routes/reviews.py`)
- **POST `/reviews/<book_id>`**
  - 輸入：書籍 id 及表單（rating 1-5、content）。
  - 邏輯：驗證資料後建立新 Review，失敗的話可能直接 Flash Error。完成後重導向至詳情頁。

### 2.4 留言與對話路由 (`app/routes/comments.py`)
- **POST `/comments/<book_id>`**
  - 輸入：書籍 id 及表單（content, 隱藏的 parent_id）。
  - 邏輯：建立 Comment，完成後重導向至詳情頁。

### 2.5 排行榜路由 (`app/routes/ranking.py`)
- **GET `/ranking`**
  - 輸入：無
  - 邏輯：依照評分的平均值做排序與聚合，顯示排行榜。
  - 輸出：渲染 `ranking.html`。

### 2.6 本月新書路由 (`app/routes/new_books.py`)
- **GET `/new-books`**
  - 輸入：無
  - 邏輯：篩選出本月份新增的新書。
  - 輸出：渲染 `new_books.html`。

## 3. Jinja2 模板清單

所有的模板將位於 `app/templates/` 中。

1. **`base.html`**：基底結構（含 `<html>`、Navbar 導覽列與 Footer），其餘頁面繼承此版面。
2. **`index.html`**（繼承 `base.html`）：首頁畫面。
3. **`books/list.html`**（繼承 `base.html`）：書籍列表畫面，具備搜尋框。
4. **`books/detail.html`**（繼承 `base.html`）：書籍詳細畫面，包含心得、表單與留言板區塊。
5. **`books/create.html`**（繼承 `base.html`）：新增專用的表單頁面。
6. **`books/edit.html`**（繼承 `base.html`）：編輯專用的表單頁面。
7. **`ranking.html`**（繼承 `base.html`）：顯示排名列表。
8. **`new_books.html`**（繼承 `base.html`）：顯示新增書籍。
