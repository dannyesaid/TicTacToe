import pygame
import time
'''rectangular left and tops.
                              (1,1)     (2,1)    (3,1)
                              (1,2)     (2,2)    (3,2)
                              (1,3)     (2,3)    (3,3) '''


pygame.init()


first_player = 'Danny'
second_player = 'Justine'
players_turn = first_player


white = pygame.Color( 255, 255, 255 )
black = pygame.Color( 0, 0, 0 )
gold = pygame.Color( 255, 215, 0 )

playing_square_one_one = pygame.Rect( 118, 110, 120, 120 )
playing_square_two_one = pygame.Rect( 238, 110, 120, 120 )
playing_square_three_one = pygame.Rect( 358, 110, 120, 120 )

playing_square_one_two = pygame.Rect( 118, 230, 120, 120 )
playing_square_two_two = pygame.Rect( 238, 230, 120, 120 )
playing_square_three_two = pygame.Rect( 358, 230, 120, 120 )

playing_square_one_three = pygame.Rect( 118, 350, 120, 120 )
playing_square_two_three = pygame.Rect( 238, 350, 120, 120 )
playing_square_three_three = pygame.Rect( 358, 350, 120, 120 )

coordinates_record = [ [playing_square_one_one,    playing_square_two_one,   playing_square_three_one],
                     [playing_square_one_two,      playing_square_two_two,   playing_square_three_two],
                     [playing_square_one_three,    playing_square_two_three, playing_square_three_three]  ]

game_record = [ [ None, None, None],
                [ None, None, None],
                [ None, None, None] ]


display_surface = pygame.display.set_mode( ( 600, 600 ),pygame.RESIZABLE   )
display_surface.fill( white )
board_image = pygame.image.load( 'Dependencies\\board.png' )
display_surface.blit( board_image, ( 90, 80 ) )
pygame.display.update()

pygame.display.toggle_fullscreen()

pygame.mixer.music.load('Dependencies\\monkeys.mp3')
pygame.mixer.music.set_volume( 0.25 )
pygame.mixer.music.play(-1,10)

first_player_sound = pygame.mixer.Sound('Dependencies\\player_one_sound.ogg')
first_player_sound.set_volume(1.0)
second_player_sound = pygame.mixer.Sound('Dependencies\\player_two_sound.ogg')
second_player_sound.set_volume(1.0)
image_one = pygame.image.load( 'Dependencies\\player_one.jpg ')
image_one_rec_scale = pygame.transform.scale( image_one, (120,120) )

image_two = pygame.image.load( 'Dependencies\\player_two.jpg' )
image_two_rec_scale = pygame.transform.scale( image_two, (120, 120) )


while True:
    mouse_position = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    game_won = False

    if any( mouse_pressed ) :
        break_outer_loop = False
        for outer in range( len( game_record ) ):
            if break_outer_loop == True:
                break

            for inner in range( len( game_record[ outer ] ) ):
                if coordinates_record[ outer ][ inner ].collidepoint( mouse_position ):
                    if game_record[ outer ][ inner ] != None:
                        break_outer_loop = True
                        break

                    if players_turn == first_player:
                        display_surface.blit( image_one_rec_scale , coordinates_record[ outer ][ inner ] )
                        pygame.display.update()

                        first_player_sound.play()

                    else:
                        display_surface.blit( image_two_rec_scale , coordinates_record[ outer ][ inner ] )
                        pygame.display.update()

                        second_player_sound.play()

                    game_record[ outer ][ inner ] = players_turn

                    if players_turn == first_player:
                        players_turn = second_player
                    else:
                        players_turn = first_player

                    break_outer_loop = True
                    break

        pygame.time.wait(300)


    winning_combinations = [
        [ game_record[0][0], game_record[1][0], game_record[2][0] ], #row one
        [ game_record[0][1], game_record[1][1], game_record[2][1] ], #row two
        [ game_record[0][2], game_record[1][2], game_record[2][2] ], #row three

        [ game_record[0][0], game_record[0][1], game_record[0][2] ], #column one
        [ game_record[1][0], game_record[1][1], game_record[1][2] ], #column two
        [ game_record[2][0], game_record[2][1], game_record[2][2] ], #column three

        [ game_record[0][0], game_record[1][1], game_record[2][2] ], #diagonal one
        [ game_record[2][0], game_record[1][1], game_record[0][2] ] #diagonal two
                                                                        ]

    for combination in winning_combinations:
        if len( set( combination ) ) == 1 and combination[0] != None:
            if players_turn == first_player:
                display_surface.blit( pygame.transform.scale( image_two, (600,600) ), (0,0)  )

            else:
                display_surface.blit( pygame.transform.scale( image_one, (600,600) ), (0,0)  )

            pygame.mixer.music.stop()
            first_player_sound.stop()
            second_player_sound.stop()
            pygame.mixer.music.load( 'Dependencies\\Queen - We Are The Champions Lyrics.mp3' )
            pygame.mixer.music.play(0, 50)

            pygame.display.update()
            time.sleep( 25 )
            pygame.mixer.music.stop()

            display_surface = pygame.display.set_mode( ( 600, 600 ) )
            display_surface.fill( white )
            board_image = pygame.image.load( 'Dependencies\\board.png' )
            display_surface.blit( board_image, ( 90, 80 ) )
            pygame.display.update()

            pygame.mixer.music.load('Dependencies\\monkeys.mp3')
            pygame.mixer.music.play(-1,10)


            game_record = [ [ None, None, None],
                            [ None, None, None],
                            [ None, None, None] ]

        options_left = [ True for outer in game_record if None in outer ]

        if not any( options_left ):
            pygame.mixer.music.stop()
            time.sleep(5)

            display_surface = pygame.display.set_mode( ( 600, 600 ) )
            display_surface.fill( white )
            board_image = pygame.image.load( 'Dependencies\\board.png' )
            display_surface.blit( board_image, ( 90, 80 ) )
            pygame.display.update()

            pygame.mixer.music.load('Dependencies\\monkeys.mp3')
            pygame.mixer.music.play(-1,10)


            game_record = [ [ None, None, None],
                            [ None, None, None],
                            [ None, None, None] ]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
