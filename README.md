# Anthropic-AI-Filter-for-Vim

A Python script that will take lines visually selected in Vim and send them to the Anthropic AI API for filtering. The script will then replace the selected lines with the filtered output from the API.

## Usage
Shortcut with leader that will call the script with the visually selected lines as input. For example, you can add the following line to your `.vimrc`:

```vim
vnoremap <Leader>af :!python3 ~/Repos/Anthropic-AI-Filter-for-Vim/correct_these_lines.py<CR>
```
