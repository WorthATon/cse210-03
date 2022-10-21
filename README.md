### cse210-03

# Jumper Game

> Class Design

| **Class: Player** |                |
| :---------------- | :------------: |
| jumper:           |  **Jumper()**  |
| \_word_to_guess:  |   **Word()**   |
| terminal_service: | **Terminal()** |
| \_get_inputs():   |    **None**    |
| \_do_updates():   |    **None**    |
| \_do_outputs():   |    **None**    |

| **Class: Jumper** |                 |
| :---------------- | :-------------: |
| \__health_:       | **Int**         |
| \__image_:        | **String List** |
| is_alive():       | **Boolean**     |
| draw_jumper():    |  **None**       |
| take_health():    |  **None**       |

| **Class: Word** |             |
| :-------------- | :---------: |
| \_text:         | **String**  |
| is_guessed():   | **Boolean** |
| draw_word():    |  **None**   |
| check_guess():  |  **None**   |

| **Class: Terminal** |          |
| :------------------ | :------: |
| show_propmt():      | **None** |
| read_text():        | **None** |
| write_text():       | **None** |
