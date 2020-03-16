# ReviewTests

## Sort Stack.
### Algorithm:
1. Tạo 1 ngăn xếp tạm: tmp_stack
2. Trong khi input_stack là NOT empty:
   * Pop một phần tử từ input_stack và gán nó là tmp.
   * Trong khi tmp_stack NOT empty và đỉnh tmp_stack lớn hơn tmp, pop 1 phần tử từ tmp_stack và push nó vào input_stack.
   * push tmp vào trong tmp_stack.

3. Sau khi hoàn thành vòng lặp đến phần tử cuối cùng: tmp_stack chính là stack đã được sắp xếp.
### Độ phức tạp của thuật toán:
O(n) = n * (n - 1)
___
## Auto complete Search.
### Mô tả ý tưởng:
   * Xử lý database: Với mỗi câu trong CSDL thì tạo bộ đếm (counter) để đánh index.
   * Tách input_string thành các từ.
   * Với mỗi từ: kiểm tra prefix. Nếu tồn tại trong câu thì trả về counter của từ đó.
   * Lấy ra top 3 câu có tổng counter lớn nhất.
