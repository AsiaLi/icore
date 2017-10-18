@echo off
set a=%cd: =:%
set a=%a:\= %
for %%j in (%a%) do (set a=%%j)
set a=%a::= %
title %a%

if "%1" == "" (
	set PORT=8004
) else (
	set PORT=%1
)

set _REGISTER_SERVICE=1

python manage.py runserver 0.0.0.0 %PORT%
