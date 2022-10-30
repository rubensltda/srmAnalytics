set original_dir=%CD%

::set venv_root_dir=%UserProfile%\files\IDB\srm_analytics\venv
set venv_root_dir=%UserProfile%\local\srmAnalytics\venv

call %venv_root_dir%\Scripts\activate.bat

python src/run_thread_keep_bloomberg_alive.py

call %venv_root_dir%\Scripts\deactivate.bat
cd %original_dir%

exit /B 1