# Bài 4: Các kiểu dữ liệu số và câu lệnh vào - ra đơn giản

## Bài 1: Tam giác vuông

Viết chương trình thực hiện nhập từ bàn phím hai số nguyên dương b, c là độ dài hai cạnh góc vuông của tam giác vuông ABC, tính và đưa ra màn hình:

- Diện tích tam giác
- Độ dài cạnh huyền

### 1. Phân tích đề bài

Các bạn thấy đó, đề bài cho mình 2 số nguyên dương b và c chính là 2 cạnh góc vuông và hỏi S và cạnh a (cạnh huyền) bằng bao nhiêu.

Trước tiên, ta cần nhớ công thức tính diện tích tam giác vuông và cạnh huyền.

- S = 1/2bc (1/2 2 cạnh góc vuông)
- a^2 = b^2 + c^2 => a = √(b^2 + c^2) (Định lý Pythagoras)

### 2. Code

Tới đây là coi như đã giải quyết xong bài toán, giờ chỉ việc tính toán thôi :>

Đầu tiên thì mình cần người dùng nhập vào 2 giá trị là b và c:

```
b = int(input("b = ")) # Thông báo yêu cầu người dùng nhập 2 số b và c
c = int(input("c = "))
```

Thì có nhiều anh em hỏi tại sao dòng "b = " lại không ghi giống trong sách là "b = 3", thì "b = " là một **dòng thông báo**, nghĩa là nó sẽ in lên màn hình để người dùng biết thông tin cần nhập vào máy. Sau khi nhập số 3 thì nó sẽ giống với trong sách ngay:

```
# Terminal:
b = 
Lúc này nó sẽ chờ bạn nhập số b vào
b = 3
Sau khi nhập số b (3) thì nó sẽ trông như thế, giống với Input chưa :)
```

Tại sao mình lại sử dụng `int(input())` thay vì `input()` thôi. Vì khi gán giá trị nhập vào từ hàm `input()` bản chất nó sẽ không phải ở dạng là một **số nguyên** mà là một chuỗi (`string`). Với các phép toán như cộng, trừ, nhân, chia, thì chuỗi sẽ không thể làm được.

```
a = "1"
b = 1
print(a*2) # In ra màn hình là 11 vì nó sẽ nhân đôi chuỗi "1" lên chứ không phải là lấy số 1
print(b*2) # In ra màn hình là số 2 vì nó là số nguyên, có thể cộng trừ nhân chia
```

`int()` ở đây được gọi là hàm **ép kiểu**. Nó sẽ ép kiểu chuối về số nguyên để có thể tính toán một cách chính xác .

Tiếp đến mình sẽ định nghĩa thêm một biến `s` lưu kết quả là diện tích của tam giác ABC.

```
s = 1/2*b*c
```

Tiếp đến là biến `a` để lưu giá trị là độ dài cạnh `a` (huyền) trong tam giác ABC.

Nhưng khoan, mình sẽ phải dùng cách nào để tính căn bậc 2 của `b^2 + c^2` đây ?

Đây chính là lúc mà chúng ta cần **thư viện `math`** của Python. Trong thư viện sẽ có những hàm giúp chúng ta tính toán tốt hơn, chẳng hạn như:

- Tính ƯCLN (`math.gcd()`)
- Tính căn bậc 2 (`math.sqrt()`)
- Tính giá trị tuyệt đối (`math.abs()`)

Và còn nhiều hàm khác, nhưng trong bài này mình sẽ sử dụng hàm tính căn bậc 2 (`math.sqrt()`)

Để dùng được thư viện này, bạn cần phải thêm thư viện vào file Python của bạn bằng câu lệnh sau (ngay đầu dòng):

`import math`

Bây giờ thì mình có thể tính căn bậc 2 của b^2 + c^2 được rồi XD.

`a = math.sqrt(b**2+c**2)`

Có nhiều ông thắc mắc là sao không dùng "^" mà lại dùng "**", thì trong Python, để viết được a^b thì ta phải viết `a**b` thì Python nó mới hiểu đây là lũy thừa.

Sau khi chúng ta giải quyết được 2 câu hỏi, chúng ta in ra màn hình kết quả hay giá trị của 2 biến lưu kết quả là `s` và `a`:

```
print("Diện tích tam giác: ", s)
print("Độ dài cạnh huyền: ", a)
```

Dấu "," là để ngăn cách giữa **biến** và **dòng thông báo** để nó có thể in ra cả thông báo là giá trị của biến cùng một lúc.

Full code:

```
import math

b = int(input("b = "))
c = int(input("c = "))

s = 1/2*b*c
a = math.sqrt(b**2+c**2)

print("Diện tích tam giác: ", s)
print("Độ dài cạnh huyền: ", a)
```

## Bài 2: Chia mận

Cô giáo đi du lịch ở Sa Pa mang về túi mận làm quá cho cả lớp. Túi mận có k quả. lớp có n học sinh. Mân được chia đều để em nào cũng nhận được một số lượng quả như nhau. Nếu còn thừa, những quả còn lại sẽ được dành cho các em nữ.

Viết chương trình: Nhập n và k vào từ bàn phím, đưa ra màn hình số quả mận mỗi học sinh nhận được và số quả dành riêng cho các em nữ. Sử dụng *dòng thông báo* cho dữ liệu nhập và và mỗi kết quả đưa ra.

### 1. Phân tích đề bài
Đề bài cho biết có `n` học sinh và `k` quả mận. Việc của mình là xác định mỗi học sinh được bao nhiêu quả mận và còn dư bao nhiêu để còn dành cho các bạn nữ.

Để chia đều số mận cho từng ấy học sinh thì đơn giản ta sẽ lấy `k/n` thôi thì sẽ ra bao nhiêu quả mận cho 1 học sinh.

Nhưng vấn đề là chúng ta cần thêm số dư để xem thử còn chia cho mấy bạn nữ được không. Nhưng trong Python thì khi bạn chia như vậy thì bạn sẽ không thể biết phép chia đó dư bao nhiêu.

```
print(16/5) # 3.2 
# Các bạn sẽ không biết nó dư bao nhiêu.
```

Vì vậy để giải quyết bài này thì ta sẽ chỉ lấy số nguyên, chính là số mận mà mỗi học sinh được nhận và không lấy phần dư (thập phân).

Còn phần dư chúng ta sẽ tính để biết còn bao nhiêu quả mận để chia lại cho các bạn nữ.

### 2. Code

Tới đó thì chúng ta đã có được hướng giải rồi, nên sẽ bắt đầu làm nha XD.

Đầu tiên thì chúng ta cần 2 biến `n` và `k` lần lượt là số học sinh và số mận.

```
n = int(input("Số học sinh: n = "))
k = int(input("Số mận:      k = "))
```

Tiếp đến, mình lưu 2 biến lần lượt tên là `moi_hs` và `con_du` để lưu lần lượt là số mận mỗi học sinh và số mận còn dư.

Trong Python, để có thể chia lấy phần nguyên (số đứng trước dấu ".") thì thay vì chia theo kiểu `16/5` thì chúng ta sẽ dùng toán tử `//`:  `16//5`.

Còn muốn chia lấy phần dư, ta sử dụng toán tử `%` để tính phần dư của phép chia: `16 % 5`.
```
moi_hs = k//n
con_du = k % n
```

Tới đây thì mình đã giải quyết xong 2 câu hỏi của đề nên mình sẽ in dòng thông báo ra:

```
print("Mỗi học sinh được chia",moi_hs,"quả mận.")
print("Số mận dành riêng cho các em nữ là", con_du)
```

Như mình đã nói trong bài **Tam giác vuông**, dấu "," dùng để ngăn cách giữa **dòng thông báo** và **biến**, nên chúng ta có thể sử dụng nhiều dấu phẩy để ngăn cách giúp chúng ta linh hoạt hơn trong việc thông báo lên màn hình hơn.

Full Code: 

```
n = int(input("Số học sinh: n = "))
k = int(input("Số mận:      k = "))

moi_hs = k//n
con_du = k % n


print("Mỗi học sinh được chia",moi_hs,"quả mận.")
print("Số mận dành riêng cho các em nữ là", con_du)
```
## Bài 3: Tính số bàn học
Trường mới đẹp và rộng hơn trường cũ, số phòng học cũng nhiều hơn so với trước. Nhà trường dự định tuyển thêm học sinh cho ba lớp mới với số lượng học sinh mỗi lớp lần lượt là a, b và c. Cần mua bàn cho cách lớp mới này. Mỗi bàn học có không quá hai chỗ ngồi cho học sinh. Xác định số lượng bàn tối thiểu cần mua.

Bạn hãy viết chương trình giải quyết bài toán trên. Dữ liệu được nhập vào từ bàn phím. Kết quả được in ra màn hình.

### 1. Phân tích bài toán
Chúng ta sẽ xem đề bài cho mình cái gì, đầu tiên là số học sinh 3 lớp(`a`, `b`, `c`), và mỗi bàn chỉ có thể cho 2 học sinh ngồi chung. Thứ chúng ta cần tính là số bàn cần mua.

Bài này nếu nghĩ đơn giản thì cũng đơn giản, chúng ta chỉ cần lấy tổng số học sinh mỗi lớp chia 2 rồi cộng lại thôi.

`a/2 + b/2 + c/2`

Nhưng từ từ đã, số bàn chúng ta không thể là số thập phân đúng không.

Mình ví dụ nhá, nếu trường có tổng số học sinh 1 lớp là 17 học sinh thì theo công thức chúng ta sẽ có:

`17/2` = 8.5 

Vậy chúng ta sẽ cần 8.5 cái bàn ? Rõ ràng là không thể cắt đôi bàn ra để chia rồi đúng không. Vậy thì cách để mình tối ưu hóa chính là cho bạn bị dư ra ngồi một bàn riêng, nghĩa là mình sẽ làm tròn kết quả lên (`8.5` -> `9`).

Tới đây thì 16 bạn đầu tiên sẽ ngồi trong 8 bàn đầu tiên, và bạn cuối cùng sẽ ngồi bàn thứ 9 một mình.

Tới đây thì mình sẽ có một công thức: 

`a/2 + b/2 + c/2` 
- Nếu là số thập phân thì làm tròn lên

### 2. Code
Tới đây mình đã trả lời được câu hỏi của đề bài nên chúng ta sẽ bắt đầu viết code.

Đầu tiên, mình cần người dùng nhập số học sinh mỗi lớp:

```
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
```

Tiếp theo, mình sẽ tính số bàn theo công thức:

`a/2 + b/2 + c/2`

Nhưng chúng ta cần làm tròn lên, nên chúng ta sẽ sử dụng hàm `math.ceil()` trong thư viện `math`.

`math.ceil()` sẽ làm tròn số thập phân lên (`8.5` -> `9`)

Trước tiên, để dùng được hàm đó, hãy nhớ thêm `import math` mới dùng được nha.

Tới đây chúng ta sẽ sử dụng biến `so_ban` để lưu kết quả:

`so_ban = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)`

Tới đây chúng ta đã có kết quả, giờ mình sẽ in kết quả ra màn hình:

`print("Số bàn tối thiểu cần mua là:", so_ban)`

Full code:

```
import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

so_ban = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)

print("Số bàn tối thiểu cần mua là:", so_ban)
```