# 🚀 happy-laborer 😀

## setup project

vscode config

```json
{
  // .vscode/launch.json
  // 使用 IntelliSense 了解相关属性。 
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

```json
{
  // .vscode.settings.json
  "python.defaultInterpreterPath": "/path/to/python",
  "python.envFile": "${workspaceFolder}/.env",
  "python.linting.pylintEnabled": false,
  "python.linting.enabled": true,
  "python.linting.pycodestyleEnabled": true,
}
```


```ini
# .env
PYTHONPATH=<absolute-project-path>
```

## Get start

dimen/scale.py

```bash
python dimen/scale.py 0.9 0.93 0.88 # 缩放dimen资源
```
