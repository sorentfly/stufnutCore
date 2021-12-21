# Запуск

## windows
Необходимо выполнить команду в консоли `venv\bin\activate` для запуска виртуальной среды.

### Если есть ошибки
#### Ошибка скриптов

` Невозможно загрузить файл A:\github\stufnutCore\venv\bin\Activate.ps1, так как выполнение сценариев отключено в этой системе. Для получения дополнительных сведений см. about_Execution_Policies по адресу http://go.microsoft.com/fwlink/?LinkID=135170.`

#### Решение
Запустите PowerShell.exe и далее `Get-ExecutionPolicy -List` `==>` `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser` `==>` `Get-ExecutionPolicy -List`.
