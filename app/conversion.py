
def conversion_3D_4D():
    origin = img_pt.GetOrigin()
    direction = img_pt.GetDirection()
    spacing = img_pt.GetSpacing()

    img_mask_array = sitk.GetArrayFromImage(img_mask)
    mask_3D=img_mask_array[1,:,:,:]
    mask_3D=GetImageFromArray(mask_3D)

    mask_3D.SetOrigin(origin)
    mask_3D.SetSpacing(spacing)
    mask_3D.SetDirection(direction)