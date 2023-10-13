## Bài 4: Các kiểu dữ liệu số và câu lệnh vào - ra đơn giản

### Bài 1: Tam giác vuông
Viết chương trình thực hiện nhập từ bàn phím hai số nguyên dương b, c là độ dài hai cạnh góc vuông của tam giác vuông ABC, tính và đưa ra màn hình:
- Diện tích tam giác
- Độ dài cạnh huyền
#### 1.Phân tích đề bài
Các bạn thấy đó, đề bài cho mình 2 số nguyên dương b và c chính là 2 cạnh góc vuông và hỏi S và cạnh a (cạnh huyền) bằng bao nhiêu.

Trước tiên, ta cần nhớ công thức tính diện tích tam giác vuông và cạnh huyền.

- S = 1/2bc (1/2 2 cạnh góc vuông)
- a^2 = b^2 + c^2 => a = √(b^2 + c^2) (Định lý Pythagoras)

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