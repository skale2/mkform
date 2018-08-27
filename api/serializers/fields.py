from rest_framework import serializers
from forms.models.fields import (
    Field,
    ShortAnswer,
    LongAnswer,
    Number,
    Boolean,
    Choice,
    MultipleChoice,
    Date,
    Time,
    DateTime,
    File,
)


DEFAULT_FIELDS = ['value', 'definition']


class ShortAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortAnswer
        fields = DEFAULT_FIELDS


class LongAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongAnswer
        fields = DEFAULT_FIELDS


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = DEFAULT_FIELDS


class BooleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boolean
        fields = DEFAULT_FIELDS


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = DEFAULT_FIELDS


class MultipleChoiceSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = MultipleChoice
        fields = DEFAULT_FIELDS  + ['choices']

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        multiple_choice = MultipleChoice.objects.create(**validated_data)

        for choice in choices:
            Choice.objects.create(multiple_choice=multiple_choice, **choice)

        return multiple_choice


class MultipleChoiceGridSerializer(serializers.ModelSerializer):
    choice_rows = MultipleChoiceSerializer(many=True)

    class Meta:
        model = MultipleChoice
        fields = DEFAULT_FIELDS + ['choice_rows']
    
    def create(self, validated_data):
        choice_rows = validated_data.pop('choice_rows')
        multiple_choice_grid = MultipleChoiceGrid.objects.create(**validated_data)

        for choice_row in choice_rows:
            MultipleChoiceSerializer.create(None, validated_data={
                'grid': multiple_choice_grid, 
                **choice_row,
            })

        return multiple_choice_grid


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = DEFAULT_FIELDS


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = DEFAULT_FIELDS


class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = DEFAULT_FIELDS


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = DEFAULT_FIELDS