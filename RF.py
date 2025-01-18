import numpy as np
from osgeo import gdal, osr
import pandas as pd

# 文件路径设置
csv_file_path = 'E:/RF/lai_predictions.csv'  # 确保路径正确
output_tiff_path = 'E:/RF/lai_predictions.tif'

# 读取 CSV 文件
data = pd.read_csv(csv_file_path, header=None)  # 假设 CSV 文件没有列头

# 将数据转换为 NumPy 数组
C = data.to_numpy()

# 获取矩阵的行列数
rows, cols = C.shape

# 创建 GeoTIFF 文件
driver = gdal.GetDriverByName("GTiff")
dataset = driver.Create(output_tiff_path, cols, rows, 1, gdal.GDT_Float32)

# 设置地理参考信息（如果有）
# 例如，如果你有原始栅格的投影和地理变换，可以在此处设置：
# geotransform = (originX, pixelWidth, 0, originY, 0, pixelHeight)
# dataset.SetGeoTransform(geotransform)
# srs = osr.SpatialReference()
# srs.ImportFromEPSG(4326)  # 例如使用WGS84坐标系
# dataset.SetProjection(srs.ExportToWkt())

# 将数据写入 TIFF 文件
band = dataset.GetRasterBand(1)
band.WriteArray(C)

# 设置 NoData 值（可选）
band.SetNoDataValue(-9999)

# 刷新缓存并关闭数据集
band.FlushCache()
dataset = None

print(f"GeoTIFF 文件已成功保存到 {output_tiff_path}")
