{{- define "mychart.fetch_highest_version" -}}
{{- $repository := index . 0 -}}
{{- include "mychart.shell" (list "python" "get_highest_version.py" $repository) -}}
{{- end -}}

{{- define "mychart.shell" -}}
{{- list "sh" "-c" (include "mychart.shell_command" .) -}}
{{- end -}}

{{- define "mychart.shell_command" -}}
{{- join " " . -}}
{{- end -}}
