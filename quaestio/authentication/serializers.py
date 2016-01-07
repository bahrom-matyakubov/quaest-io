from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first', 'last', 'battle_cry', 'password', 'confirm_password')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, account, validated_data):
        account.username = validated_data.get('username', account.username)
        account.battle_cry = validated_data.get('battle_cry', account.battle_cry)
        account.save()
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            account.set_password(password)
            account.save()

        update_session_auth_hash(self.context.get('request'), account)

        return account

