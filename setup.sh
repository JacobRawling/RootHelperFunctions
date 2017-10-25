echo "Configuring .bash_profile to append PYTHON PATH.." 
echo "export ROOT_HELPER_FUNCS_PATH=$PWD" >> ~/.bash_profile
export ROOT_HELPER_FUNCS_PATH=$PWD
echo "export PYTHON_PATH=$ROOT_HELPER_FUNCS_PATH:$PYTHON_PATH" >> ~/.bash_profile
export PYTHON_PATH=$ROOT_HELPER_FUNCS_PATH:$PYTHON_PATH
echo "done." 

## Should exist 
if [ -z ${ATLAS_STYLE_PATH+x} ]; then
	echo "CHECKING OUT ATLAS STYLE DEPENDENCY!" 
	git clone https://github.com/JacobRawling/ATLASStyle.git ATLASStyle
	source ATLASStyle/setup.sh 
else
 echo "ATLASStyle python package found."
fi
