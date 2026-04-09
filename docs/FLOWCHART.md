# 流程圖設計 — 讀書筆記本系統

## 1. 系統總覽流程圖

使用者進入系統後的整體導覽流程：

```mermaid
flowchart TD
    Start([使用者開啟網站]) --> Home[首頁]
    Home --> Nav{導覽列選擇}

    Nav --> |書籍列表| BookList[書籍列表頁<br/>/books]
    Nav --> |推薦排行榜| Ranking[推薦排行榜<br/>/ranking]
    Nav --> |本月新書| NewBooks[本月新書<br/>/new-books]
    Nav --> |新增書籍| CreateBook[新增書籍<br/>/books/new]

    BookList --> Search{使用搜尋？}
    Search --> |是| SearchResult[顯示搜尋結果]
    Search --> |否| BrowseList[瀏覽書籍列表]
    SearchResult --> BookDetail[書籍詳細頁<br/>/books/id]
    BrowseList --> BookDetail

    BookDetail --> Action{選擇操作}
    Action --> |撰寫心得| WriteReview[撰寫心得與評分]
    Action --> |留言提問| WriteComment[詢問對話框留言]
    Action --> |編輯書籍| EditBook[編輯書籍<br/>/books/id/edit]
    Action --> |刪除書籍| DeleteBook[刪除書籍]

    Ranking --> BookDetail
    NewBooks --> BookDetail

    CreateBook --> BookDetail

    WriteReview --> BookDetail
    WriteComment --> BookDetail
    EditBook --> BookDetail
    DeleteBook --> BookList
```

---

## 2. 功能流程圖

### 2.1 F1：記錄書名（書籍 CRUD）

#### 新增書籍

```mermaid
flowchart TD
    A([使用者點擊「新增書籍」]) --> B[顯示新增書籍表單]
    B --> C[填寫書籍資訊<br/>書名/作者/出版社/出版日期/ISBN]
    C --> D[點擊「送出」]
    D --> E{表單驗證}
    E --> |通過| F[寫入資料庫]
    F --> G[顯示成功訊息]
    G --> H[重導向至書籍詳細頁]
    E --> |未通過| I[顯示錯誤提示]
    I --> B
```

#### 編輯書籍

```mermaid
flowchart TD
    A([使用者在詳細頁點擊「編輯」]) --> B[顯示編輯表單<br/>預填現有資料]
    B --> C[修改書籍資訊]
    C --> D[點擊「儲存」]
    D --> E{表單驗證}
    E --> |通過| F[更新資料庫]
    F --> G[顯示成功訊息]
    G --> H[重導向至書籍詳細頁]
    E --> |未通過| I[顯示錯誤提示]
    I --> B
```

#### 刪除書籍

```mermaid
flowchart TD
    A([使用者點擊「刪除」]) --> B{確認刪除？}
    B --> |確認| C[從資料庫刪除書籍<br/>及其相關心得與留言]
    C --> D[顯示成功訊息]
    D --> E[重導向至書籍列表]
    B --> |取消| F[返回書籍詳細頁]
```

---

### 2.2 F2：詢問對話框

```mermaid
flowchart TD
    A([使用者進入書籍詳細頁]) --> B[載入留言列表<br/>依時間排序]
    B --> C{使用者操作}

    C --> |新增留言| D[在對話框輸入內容]
    D --> E[點擊「送出留言」]
    E --> F{內容驗證}
    F --> |通過| G[寫入留言至資料庫]
    G --> H[重新載入留言列表]
    F --> |未通過| I[顯示錯誤提示<br/>內容不可為空]
    I --> D

    C --> |回覆留言| J[點擊某則留言的「回覆」]
    J --> K[顯示回覆輸入框]
    K --> L[輸入回覆內容]
    L --> M[點擊「送出回覆」]
    M --> N{內容驗證}
    N --> |通過| O[寫入回覆至資料庫<br/>關聯 parent_id]
    O --> H
    N --> |未通過| P[顯示錯誤提示]
    P --> K

    H --> C
```

---

### 2.3 F3：心得與評分

```mermaid
flowchart TD
    A([使用者進入書籍詳細頁]) --> B[載入心得列表<br/>顯示平均評分]
    B --> C{使用者操作}

    C --> |撰寫心得| D[點擊「撰寫心得」]
    D --> E[選擇評分<br/>1-5 星]
    E --> F[輸入心得內容]
    F --> G[點擊「送出」]
    G --> H{驗證}
    H --> |通過| I[寫入心得至資料庫]
    I --> J[更新平均評分]
    J --> K[重新載入心得列表]
    H --> |未通過| L[顯示錯誤提示<br/>評分與心得皆為必填]
    L --> E

    C --> |瀏覽心得| M[捲動瀏覽心得列表<br/>依時間倒序排列]
    K --> C
```

---

### 2.4 F4：推薦書籍排行榜

```mermaid
flowchart TD
    A([使用者點擊「推薦排行榜」]) --> B[查詢資料庫<br/>計算所有書籍平均評分]
    B --> C[依平均評分由高至低排序]
    C --> D[取前 10 名]
    D --> E[顯示排行榜頁面<br/>排名/書名/作者/平均評分/評論數]
    E --> F{使用者操作}
    F --> |點擊書名| G[跳轉至該書籍詳細頁]
    F --> |繼續瀏覽| E
```

---

### 2.5 F5：本月新書

```mermaid
flowchart TD
    A([使用者點擊「本月新書」]) --> B[取得當前年月]
    B --> C[查詢資料庫<br/>篩選本月建立的書籍]
    C --> D{有本月新書？}
    D --> |有| E[以卡片形式顯示<br/>書名/作者/新增日期]
    D --> |無| F[顯示「本月尚無新書」提示]
    E --> G{使用者操作}
    G --> |點擊書籍卡片| H[跳轉至該書籍詳細頁]
    G --> |繼續瀏覽| E
```

---

### 2.6 F6：書籍搜尋

```mermaid
flowchart TD
    A([使用者進入書籍列表頁]) --> B[顯示搜尋列與書籍列表]
    B --> C[使用者輸入搜尋關鍵字]
    C --> D[送出搜尋請求]
    D --> E[後端模糊比對<br/>書名 LIKE 或 作者 LIKE]
    E --> F{有符合結果？}
    F --> |有| G[顯示搜尋結果列表<br/>書名/作者/平均評分]
    F --> |無| H[顯示「查無結果」提示]
    G --> I{使用者操作}
    I --> |點擊結果| J[跳轉至該書籍詳細頁]
    I --> |修改關鍵字| C
    H --> C
```

---

## 3. 頁面導覽流程圖

```mermaid
flowchart LR
    Home["🏠 首頁<br/>/"]
    BookList["📚 書籍列表<br/>/books"]
    BookNew["➕ 新增書籍<br/>/books/new"]
    BookDetail["📖 書籍詳細頁<br/>/books/id"]
    BookEdit["✏️ 編輯書籍<br/>/books/id/edit"]
    Ranking["🏆 推薦排行榜<br/>/ranking"]
    NewBooks["🆕 本月新書<br/>/new-books"]

    Home --> BookList
    Home --> Ranking
    Home --> NewBooks

    BookList --> BookNew
    BookList --> BookDetail

    BookDetail --> BookEdit
    BookDetail --> BookList

    BookNew --> BookDetail
    BookEdit --> BookDetail

    Ranking --> BookDetail
    NewBooks --> BookDetail
```

---

## 4. 資料流向圖

```mermaid
flowchart TD
    subgraph 使用者介面
        UI_Form[表單輸入<br/>書籍/心得/留言]
        UI_Search[搜尋輸入]
        UI_Display[頁面顯示]
    end

    subgraph Flask 後端
        Route[路由處理<br/>Controller]
        Validate[資料驗證]
        Query[資料查詢]
    end

    subgraph 資料庫
        DB_Books[(books 資料表)]
        DB_Reviews[(reviews 資料表)]
        DB_Comments[(comments 資料表)]
    end

    UI_Form --> |POST| Route
    UI_Search --> |GET with query| Route
    Route --> Validate
    Validate --> |寫入| DB_Books
    Validate --> |寫入| DB_Reviews
    Validate --> |寫入| DB_Comments
    Route --> Query
    Query --> |讀取| DB_Books
    Query --> |讀取| DB_Reviews
    Query --> |讀取| DB_Comments
    Query --> |回傳資料| UI_Display
    Validate --> |驗證失敗| UI_Display
```
