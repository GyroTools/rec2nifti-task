import nibabel as nib
import numpy as np

recfile = r'{{ inputs.in1.rec.path }}'
outfile = r'{{ output_dir }}/{{ inputs.in1.rec.basename }}.nii'

img = nib.load(recfile)
flipped_data = np.flip(img.get_fdata(), axis=1)
nifti = nib.Nifti1Image(flipped_data, img.affine, header=img.header)
nifti.set_data_dtype('<f4')
nifti.to_filename(outfile)