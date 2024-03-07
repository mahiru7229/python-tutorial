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