def cal(dataset, source_type):
  print(f'{dataset}, {source_type}')
  total_size = 0
  count = 0
  with open(f'{dataset}/{source_type}/source') as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      total_size+=len(line.split())
      count+=1
  print(f'total_size: {total_size}')
  print(f'count {count}')
  print(f'avg {total_size / count}')
  print()
  return total_size, count
 
word_total_size = 0
word_count = 0
line_total_size = 0
line_count = 0

s, c = cal('java1000', 'word')
word_total_size += s
word_count += c
s, c = cal('java1000', 'line')
line_total_size += s
line_count += c
s, c = cal('java2000', 'word')
word_total_size += s
word_count += c
s, c = cal('java2000', 'line')   
line_total_size += s
line_count += c
s, c = cal('python1000', 'word')
word_total_size += s
word_count += c
s, c = cal('python1000', 'line')
line_total_size += s
line_count += c

print()
print('word total')
print(f'avg {word_total_size / word_count}')
print('line total')
print(f'avg {line_total_size / line_count}')
