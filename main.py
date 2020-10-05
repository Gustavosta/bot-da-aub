# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('O bot se conectou ao discord como: {0.user}'.format(client))

@client.event
    
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('=teste'):
        await message.channel.send('Pai tá on! 😎')

    if message.content.startswith('=help'):
        await message.channel.send('Hi, se estiver com alguma dúvida, leia as regras do servidor aqui: <#761609520245637130> \nE não esqueça de ler as regras de como você deve jogar nesse servidor aqui: <#761609776151920712> \n\nTenha um bom jogo e se divirta!')


newUserDMMessage = "Olá, vi que você entrou no Among Us Brasil (AUB), então seja bem-vindo(a)!\nEu sou o bot da AUB e vim te avisar para você não esquecer de ler as regras do servidor e as regras de como jogar Among Us no nosso servidor!\n\nQue você tenha um bom jogo! :)"


@client.event
async def on_member_join(member):
    await member.send(newUserDMMessage)
    channel = client.get_channel(761596837001560128)
    await channel.send(f':closed_umbrella: Bem-vindo(a), {member.mention}! Espero que não seja um impostor :eyes:!') 

@client.event
async def on_member_remove(member):
    channel = client.get_channel(761596837001560128)
    await channel.send(f'{member.mention} se ejetou do servidor, infelizmente ele(a) não era um impostor... :tired_face:') 

client.run('NzYxNjI2NDAxOTM3NDI0Mzg0.X3dV3A.GDcEidynigswTECRhVgpc8vaT5U')
