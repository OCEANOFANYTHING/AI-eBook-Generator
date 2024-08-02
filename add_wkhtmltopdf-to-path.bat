@echo off
SET WKHTMLTOPDF_PATH=C:\Program Files\wkhtmltopdf\bin

SETX PATH "%PATH%;%WKHTMLTOPDF_PATH%"

echo wkhtmltopdf has been added to PATH.
