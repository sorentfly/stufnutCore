# ROUTES
- /
- /room/\<int:roomId>
- /base/
- /base/sex

# Запуск

## windows
- `-_-`
- `.\venv-windows\Scripts\activate` для запуска виртуальной среды.
- `cd .\core`
- `python manage.py runserver`
- `-_-`

### Если есть ошибки
#### Ошибка скриптов

` Невозможно загрузить файл A:\github\stufnutCore\venv\bin\Activate.ps1, так как выполнение сценариев отключено в этой системе. Для получения дополнительных сведений см. about_Execution_Policies по адресу http://go.microsoft.com/fwlink/?LinkID=135170.`

#### Решение
Запустите PowerShell.exe и далее `Get-ExecutionPolicy -List` `==>` `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser` `==>` `Get-ExecutionPolicy -List`.
