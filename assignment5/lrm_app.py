from lrm import LinRegModel, rmse

model_default = LinRegModel()
model_custom = LinRegModel(slope=-1, bias=4)

print(model_default)
print(model_custom)

xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ylist = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

pred_default = model_default.predict(xlist)
pred_custom = model_custom.predict(xlist)

rmse_default = rmse(pred_default, ylist)
rmse_custom = rmse(pred_custom, ylist)

print("RMSE of default model:", rmse_default)
print("RMSE of custom model:", rmse_custom)
