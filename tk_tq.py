import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "dataset/dataset-416.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Xóa các dòng có 'Mã HP' hoặc 'Học Kỳ' bị thiếu
df_cleaned = df.dropna(subset=['Mã HP', 'Học Kỳ'])

# Chuyển 'Học Kỳ' sang kiểu số nguyên (sau khi loại bỏ NaN)
df_cleaned['Học Kỳ'] = df_cleaned['Học Kỳ'].astype(int)

# Chuyển 'Học Kỳ' thành dạng 'Học kỳ X' để hiển thị rõ ràng
df_cleaned['Học Kỳ'] = df_cleaned['Học Kỳ'].apply(lambda x: f'Học kỳ {x}')

# Tạo biểu đồ Sunburst Chart
fig = px.sunburst(
    df_cleaned,
    path=['Học Kỳ', 'Loại môn học', 'Tên học phần'],  # Cấu trúc phân cấp
    title="Chương trình đào tạo - Sunburst Chart",
    color='Học Kỳ',
    color_discrete_sequence=px.colors.qualitative.Set3  # Màu sắc dễ phân biệt
)

# Lưu biểu đồ dưới dạng file HTML
output_html = "sunburst_chart.html"
fig.write_html(output_html)


