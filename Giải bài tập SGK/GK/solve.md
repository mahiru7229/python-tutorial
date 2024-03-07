## Giải bài tập tin học giữa kì I



- [Giải bài tập tin học giữa kì I](#giải-bài-tập-tin-học-giữa-kì-i)
- [1. Dạng chính](#1-dạng-chính)
- [2. Sửa bài](#2-sửa-bài)
  - [2.1 Bài 1:](#21-bài-1)
    - [2.1.1 Giải thích cách làm](#211-giải-thích-cách-làm)
    - [2.1.2 Code](#212-code)
  - [2.2 Bài 2:](#22-bài-2)
    - [2.2.1 Giải thích cách làm](#221-giải-thích-cách-làm)
    - [2.2.2 Code](#222-code)
  - [2.3 Bài 3:](#23-bài-3)
    - [2.3.1 Giải thích cách làm](#231-giải-thích-cách-làm)
    - [2.3.2 Code](#232-code)




## 1. Dạng chính

Dạng của giữa kì phần tự luận sẽ là về `string` (chuỗi, xâu).

## 2. Sửa bài

### 2.1 Bài 1: 

**Bài 1: Viết chương trình để thực hiện các công việc sau:** 
Gán xâu: 
 `s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'`. 
`y = 'n'`. 

- Xác định vị trí đầu tiên trong xâu `s` mà từ đó xâu y xuất hiện như một xâu con của xâu `s`.
- Viết câu lệnh để trích xâu con là `‘Đoàn TNCS’`
- Đưa ra độ dài của xâu `s`. 
- Cho biết xâu y xuất hiện bao nhiêu lần trong xâu `s`.

### 2.1.1 Giải thích cách làm

**1. Xác định vị trí đầu tiên trong xâu `s` mà từ đó xâu y xuất hiện như một xâu con của xâu `s`.** 

Để xác định được thì ta sẽ dùng một phương thức (gọi hàm), có cú pháp là `string.find(<str>)` 
Với `<str>` là xâu bạn muốn tìm (xâu con) trong xâu mẹ (`string`).

```
s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'
y = 'n'

pos = s.find(y) # Tìm vị trí mà xâu con y được tìm thấy tại xâu mẹ s (lấy vị trí bắt đầu) và gán cho biến pos.
print(pos) # In ra màn hình vị trí
```
***Chú ý: " " (khoảng trống, dấu cách) được tính là một kí tự.***

**2. Viết câu lệnh để trích xâu con là `'Đoàn TNCS'`** 

Để trích xâu con (cắt xâu mẹ thành một xâu con), ta dùng cú pháp `string[start:stop]`. 
Với `start` là vị trí cắt đầu tiên (vị trí đầu tiên được tính là 0), `stop` là vị trí cuối cùng mà xâu được cắt (vị trí này có giá trị thực là `stop - 1`). 

Nên để cắt được, ta cần tìm vị trí mà `'Đoàn TNCS'` xuất hiện. Vị trí đó sẽ là: 

| Kí tự  | C | h | ... | Đ  | o  | à  | n  |    | T  | N  | C  | S  |    | ... |
|--------|---|---|-----|----|----|----|----|----|----|----|----|----|----|-----|
| Vị trí | 0 | 1 | ... | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | ... |

Vậy vị trí chúng ta phải lấy từ $25$ đến $33$, nên câu lệnh chúng ta sử dụng sẽ như sau: 

```
s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'
y = 'n'

sub_s = s[25:34] # Vì stop-1 nên nó sẽ không lấy vị trí 33, nên chúng ta phải +1 để chương trình lấy luôn vị trí 33
print(sub_s) # In ra xâu con
```

**3. Đưa ra độ dài của xâu s.**

Để chương trình xác định được độ dài của xâu s, chúng ta sử dụng cú pháp `len(<str>)`. 
Với `<str>` là xâu cần được tìm độ dài. 

Vậy chương trình có dạng như sau: 

```
s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'
y = 'n'

do_dai = len(s) # Lấy độ dài của xâu s
print(do_dai) # In ra độ dài của xâu s
```

**4. Cho biết xâu y xuất hiện bao nhiêu lần trong xâu s.**

Để xem xâu `y` xuất hiện bao nhiêu lần trong xâu `s`, ta dùng cú pháp `string.count(<str>)`. 
Với `string` là xâu mẹ, `<str>` là xâu con. 

Vậy chương trình có dạng như sau: 
```
s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'
y = 'n'

count = s.count(y) # Đếm xem xâu y đã xuất hiện bao nhiêu lần trong xâu s
print(count) # In ra kết quả

```

***Chú ý: `'n'` và `'N'` là 2 kí tự hoàn toàn khác nhau (in thường và hoa là khác nhau dù cùng là một chữ)***

### 2.1.2 Code 

```
s = 'Chào mừng ngày thành lập Đoàn TNCSHCM 26/03/2023'
y = 'n'

pos = s.find(y) # Tìm vị trí mà xâu con y được tìm thấy tại xâu mẹ s (lấy vị trí bắt đầu) và gán cho biến pos.
print(pos) # In ra màn hình vị trí

sub_s = s[25:34] # Vì stop-1 nên nó sẽ không lấy vị trí 33, nên chúng ta phải +1 để chương trình lấy luôn vị trí 33
print(sub_s) # In ra xâu con

do_dai = len(s) # Lấy độ dài của xâu s
print(do_dai) # In ra độ dài của xâu s

count = s.count(y) # Đếm xem xâu y đã xuất hiện bao nhiêu lần trong xâu s
print(count) # In ra kết quả
```

### 2.2 Bài 2: 

**Bài 2: Viết chương trình tính số lượng các kí tự chữ cái.**

***Đang liên hệ cô để kiểm tra đề...***


### 2.2.1 Giải thích cách làm

### 2.2.2 Code

### 2.3 Bài 3: 

**Bài 3: Nhập vào họ tên bất kì sau đó biến đổi các chữ cái đầu tiên là in hoa**

***Và vẫn đang liên hệ cô để kiểm tra đề ...***

### 2.3.1 Giải thích cách làm

### 2.3.2 Code

