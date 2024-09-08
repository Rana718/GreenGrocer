import React from 'react';

import { View, Text, StatusBar } from 'react-native';
import Landing from '@/components/Landing';

export default function App() {
    return (
        <View className="flex-1 bg-gray-900">
            <Landing />
        </View>
    );
}
