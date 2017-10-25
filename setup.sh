echo "export ROOT_HELPER_FUNCS_PATH=$PWD" >> ~/.bash_profile
export ROOT_HELPER_FUNCS_PATH=$PWD
echo "export PYTHON_PATH=$ROOT_HELPER_FUNCS_PATH:$PYTHON_PATH" >> ~/.bash_profile
export PYTHON_PATH=$ROOT_HELPER_FUNCS_PATH:$PYTHON_PATH

## Should exist 
if [[ ! -v ATLAS_STYLE_PATH ]]; then
	echo "CHECKING OUT ATLAS STYLE DEPENDENCY!" 
	git clone https://github.com/JacobRawling/ATLASStyle.git ATLASStyle
	source ATLASStyle/setup.sh 
fi
