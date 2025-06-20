# Лабораторная работа №7

## Задание

Необходимо спроектировать диаграмму классов для онлайн-платформы, предназначенной для поиска, бронирования и оплаты туристических туров.

Последовательность выполнения задания:
1. Проанализировать предметную область (выдержку из брифинга)
2. Определить основные сущности (классы) системы
3. Определить, какие связи существуют между классами
4. Оформите диаграмму классов (используйте корректные обозначения, маркеры видимости, подпишите атрибуты и методы)

### Предметная область

Выдержка из брифинга:

- На платформе регистрируются различные пользователи. У каждого пользователя есть базовые данные для идентификации и входа в систему. Помимо обычных клиентов, существуют агенты по туризму и администраторы, обладающие расширенными правами.
- Пользователь может просматривать туры, выбирать подходящие варианты и оформлять бронирование. Каждый тур содержит информацию о маршруте, услугах, стоимости, датах и этапах путешествия.
- Тур состоит из нескольких этапов (например, перелёт, проживание, экскурсии). Этапы могут отличаться по типу, длительности и месту проведения.
- После выбора тура пользователь оформляет бронирование, указывая количество участников и дополнительные опции (например, страховка, VIP-обслуживание).
- Для подтверждения бронирования требуется оплата. Платформа поддерживает различные способы оплаты и фиксирует статус платежей.
- После завершения поездки пользователь может оставить отзыв о туре, указав текст и рейтинг.
- Агенты по туризму могут создавать и редактировать туры, а также просматривать бронирования своих клиентов.
- Администраторы управляют пользователями и следят за корректностью работы платформы.
